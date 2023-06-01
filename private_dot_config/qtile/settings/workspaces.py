"""Module that defines the qtile workspaces"""

from libqtile.config import Group

WS = [
    (" webz ", "  "),
    (" term ", "  "),
    (" code ", "  "),
    (" cale ", "  "),
    (" comm ", "  "),
    (" musi ", "  "),
    (" note ", "  "),
    (" task ", "  "),
    (" misc ", "  "),
]

GROUPS = [Group(name, label=label) for name, label in WS]
