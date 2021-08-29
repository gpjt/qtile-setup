from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.command import lazy

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

    # Mod-control-k to lock screen
    Key(["mod4", "control"], "k", lazy.spawn("gnome-screensaver-command -l")),
]
