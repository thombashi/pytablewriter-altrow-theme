from typing import Any, Dict, Optional, Union

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
    lcell: Cell, rcell: Cell, **kwargs: Dict[str, Any]
) -> Optional[Style]:
    fg_color: Union[Color, str, None] = None
    bg_color: Union[Color, str, None] = None
    row = lcell.row if lcell else rcell.row

    color = Color(kwargs.get("color", DEFAULT_COLOR))

    if row % 2 == 0:
        fg_color = _calc_other_ground_color(color)
        bg_color = color
    else:
        fg_color = color

    if fg_color or bg_color:
        return Style(color=fg_color, bg_color=bg_color)

    return None


def style_filter(cell: Cell, **kwargs: Dict[str, Any]) -> Optional[Style]:
    fg_color: Union[Color, str, None] = None
    bg_color: Union[Color, str, None] = None

    color = Color(kwargs.get("color", DEFAULT_COLOR))

    if cell.row % 2 == 0:
        fg_color = _calc_other_ground_color(color)
        bg_color = color
    else:
        fg_color = color

    if fg_color or bg_color:
        return Style(color=fg_color, bg_color=bg_color)

    return None
