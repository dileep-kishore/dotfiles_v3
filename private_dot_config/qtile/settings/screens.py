"""Module that defines the screens"""

from libqtile import bar
from libqtile.config import Screen

from .widgets import (
    windowname_widget,
    spacer_widget,
    sep_widget,
    workspace_widget,
    systray_widget,
    clock_widget,
    layout_widget,
)

SCREENS = [
    Screen(
        top=bar.Bar(
            [
                windowname_widget(),
                sep_widget("right", "focus"),
                spacer_widget(),
                workspace_widget(),
                spacer_widget(),
                sep_widget("left", "active"),
                clock_widget(),
                layout_widget(),
            ],
            35,
            margin=[0, 4, 0, 4],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                windowname_widget(),
                sep_widget("right", "focus"),
                spacer_widget(),
                workspace_widget(),
                spacer_widget(),
                systray_widget(),
                sep_widget("left", "active"),
                clock_widget(),
                layout_widget(),
            ],
            35,
            margin=[0, 4, 0, 4],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                windowname_widget(),
                sep_widget("right", "focus"),
                spacer_widget(),
                workspace_widget(),
                spacer_widget(),
                sep_widget("left", "active"),
                clock_widget(),
                layout_widget(),
            ],
            35,
            margin=[0, 4, 0, 4],
        ),
    ),
]
