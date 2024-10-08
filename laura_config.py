from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.lazy import lazy

num_stacks = 2

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(active="66ff66", inactive="006600"),
                widget.WindowName(),
                widget.Prompt(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
                widget.Systray(),
            ],
            30,
        ),
    ),
]

extra_keys = [
    Key(["mod4"], "Return", lazy.spawn("alacritty")),
]
