"""Module that define qtile widgets"""

from libqtile import bar, widget

from .theme import COLORS

left = ""
right = ""


def windowname_widget():
    w = widget.WindowName(
        font="Noto Sans Bold",
        fontsize=13,
        foreground=COLORS["bg"],
        background=COLORS["focus"],
        width=bar.CALCULATED,
        empty_group_string="Desktop",
        max_chars=80,
    )
    return w


def spacer_widget():
    w = widget.Spacer(
        background=COLORS["bg"],
        # length=20,
    )
    return w


def sep_widget(dir, color):
    w = widget.TextBox(
        text=left if dir == "left" else right,
        background=COLORS["bg"],
        foreground=COLORS[color],
        padding=0,
        fontsize=35,
    )
    return w


def workspace_widget():
    w = widget.GroupBox(
        font="Font Awesome 6 Free",
        # fontsize=18,
        margin_y=2,
        margin_x=0,
        padding_y=6,
        padding_x=4,
        disable_drag=True,
        use_mouse_wheel=True,
        active=COLORS["active"],
        inactive=COLORS["inactive"],
        # rounded=True,
        highlight_method="line",
        block_highlight_text_color=COLORS["active"],
        this_current_screen_border=COLORS["focus"],
        this_screen_border=COLORS["active"],
        other_current_screen_border=COLORS["active"],
        other_screen_border=COLORS["bg"],
        foreground=COLORS["focus"],
        background=COLORS["bg"],
        urgent_border=COLORS["urgent"],
    )
    return w


def systray_widget():
    w = widget.Systray(background=COLORS["bg"], icon_size=10, padding=5)
    return w


def clock_widget():
    w = widget.Clock(
        font="Noto Sans Bold",
        foreground=COLORS["bg"],
        background=COLORS["active"],
        fontsize=13,
        format=" %a-%d | %H:%M ",
    )
    return w


def layout_widget():
    w = widget.CurrentLayoutIcon(
        foreground=COLORS["bg"], background=COLORS["active"], scale=0.75
    )
    return w
