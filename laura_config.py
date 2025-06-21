import re
import subprocess

from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.lazy import lazy

num_stacks = 2


def active_outputs():
    """Return only outputs that are both connected _and_ have a mode set."""
    out = subprocess.run(["xrandr", "--query"], stdout=subprocess.PIPE)
    lines = out.stdout.decode().splitlines()
    return [
        line.split()[0]
        for line in lines
        if " connected " in line and re.search(r" \d+x\d+\+\d+\+\d+", line)
    ]


connected = active_outputs()

screens = []
screens.append(
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(active="66ff66", inactive="006600", fontsize=24),
                widget.WindowName(fontsize=24),
                widget.Prompt(fontsize=24),
                widget.Clock(format='%Y-%m-%d %a %H:%M', fontsize=24),
                widget.Systray(fontsize=24),
            ],
            45,
        ),
    )
)

if "DP-3-1" in connected:
    screens.append(
        Screen(
            bottom=bar.Bar(
                [
                    widget.GroupBox(active="66ff66", inactive="006600")
                ],
                30
            )
        )
    )

if "DP-3-8" in connected:
    screens.append(
        Screen(
            bottom=bar.Bar(
                [
                    widget.GroupBox(active="66ff66", inactive="006600")
                ],
                30
            )
        )
    )

extra_keys = [
    Key(["mod4"], "Return", lazy.spawn("alacritty")),
    Key(
        ["mod4"], "m",
        lazy.spawn("xrandr --output DP-3-1 --mode 1920x1200 --pos 2880x0 --rotate right"),
        lazy.spawn("xrandr --output DP-3-8 --mode 1920x1200 --pos 4080x0 --rotate right"),
        lazy.reload_config(),
        desc="Enable external monitor"
    ),
    Key(
        ["mod4"], "n",
        lazy.spawn("xrandr --output DP-3-1 --off"),
        lazy.spawn("xrandr --output DP-3-8 --off"),
        lazy.reload_config(),
        desc="Disable external monitor"
    ),
]

