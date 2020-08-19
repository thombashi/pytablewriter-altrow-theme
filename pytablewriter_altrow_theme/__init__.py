import sys
from typing import Optional, Union

from pytablewriter.style import Cell, Style
from tcolorpy import Color

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


DEFAULT_COLOR = "white"


def _calc_other_ground_color(color: Color) -> str:
    invert_threshold = 385

    if (color.red + color.green + color.blue) > invert_threshold:
        return "black"

    return "white"


def col_separator_style_filter(lcell: Cell, rcell: Cell, **kwargs) -> Optional[Style]:
    fg_color = None  # type: Union[Color, str, None]
    bg_color = None  # type: Union[Color, str, None]
    row = lcell.row if lcell else rcell.row
    col = lcell.col if lcell else rcell.col

    color = Color(kwargs.get("color", DEFAULT_COLOR))

    if row % 2 == 0:
        fg_color = _calc_other_ground_color(color)
        bg_color = color
    else:
        fg_color = color

    if fg_color or bg_color:
        return Style(color=fg_color, bg_color=bg_color)

    return None


def style_filter(cell: Cell, **kwargs) -> Optional[Style]:
    fg_color = None  # type: Union[Color, str, None]
    bg_color = None  # type: Union[Color, str, None]

    color = Color(kwargs.get("color", DEFAULT_COLOR))

    if cell.row % 2 == 0:
        fg_color = _calc_other_ground_color(color)
        bg_color = color
    else:
        fg_color = color

    if fg_color or bg_color:
        return Style(color=fg_color, bg_color=bg_color)

    return None
