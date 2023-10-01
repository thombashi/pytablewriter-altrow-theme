from typing import Any, Optional, Union

from pytablewriter.style import Cell, Style
from tcolorpy import Color

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


DEFAULT_COLOR = "white"


def _calc_other_ground_color(color: Color) -> str:
    invert_threshold = 385

    if (color.red + color.green + color.blue) > invert_threshold:
        return "black"

    return "white"


def col_separator_style_filter(
    lcell: Optional[Cell], rcell: Optional[Cell], **kwargs: Any
) -> Optional[Style]:
    fg_color: Union[Color, str, None] = None
    bg_color: Union[Color, str, None] = None

    cell = lcell if lcell else rcell
    if cell is None:
        return None

    if cell.is_header_row():
        return None

    color = Color(kwargs.get("color", DEFAULT_COLOR))

    if cell.row % 2 == 0:
        fg_color = _calc_other_ground_color(color)
        bg_color = color
    else:
        fg_color = color

    if fg_color or bg_color:
        return Style(color=fg_color, bg_color=bg_color)

    return None


def style_filter(cell: Cell, **kwargs: Any) -> Optional[Style]:
    fg_color: Union[Color, str, None] = None
    bg_color: Union[Color, str, None] = None

    if cell.is_header_row():
        return None

    color = Color(kwargs.get("color", DEFAULT_COLOR))

    if cell.row % 2 == 0:
        fg_color = _calc_other_ground_color(color)
        bg_color = color
    else:
        fg_color = color

    if fg_color or bg_color:
        return Style(color=fg_color, bg_color=bg_color)

    return None
