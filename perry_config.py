import re
import subprocess

from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.lazy import lazy

num_stacks = 3


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
# only add the HDMI-0 screen if it’s currently active
if "HDMI-0" in connected:
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

# always define the primary (DP-2)
screens.append(
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(active="66ff66", inactive="006600"),
                widget.TextBox(text="/ net:"),
                widget.Net(interface="eno3"),
                widget.TextBox(text="/ mem:"),
                widget.Memory(),
                widget.TextBox(text="/ disk:"),
                widget.DF(visible_on_warn=False, format="{f}{m}/{s}{m}"),
                widget.TextBox(text="/ cpu:"),
                widget.CPUGraph(
                    border_color="006600",
                    fill_color="66ff66",
                    graph_color="66ff66"
                ),
                widget.TextBox(text="/ temp:"),
                widget.ThermalSensor(
                    foreground="66ff66",
                    tag_sensor="Package id 0"
                ),
                widget.TextBox(text="/ win:"),
                widget.WindowName(),
                widget.Prompt(),
                widget.Volume(
                    emoji=False,
                    step=5,
                    get_volume_command="wpctl get-volume @DEFAULT_AUDIO_SINK@",
                    volume_up_command="wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+",
                    volume_down_command="wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-",
                    mute_command="wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle",
                    check_mute_command="wpctl get-volume @DEFAULT_AUDIO_SINK@",
                    check_mute_string="[MUTED]",
                ),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a'),
                widget.TextBox(text="/ PT:"),
                widget.Clock(format='%H:%M'),
                widget.TextBox(text="/ UTC:"),
                widget.Clock(format='%H:%M', timezone="UTC"),
            ],
            30,
        )
    )
)

extra_keys = [
    Key(["mod4"], "Return", lazy.spawn("alacritty")),
    # super-M → turn HDMI-0 on and reload config (adds second screen)
    Key(
        ["mod4"], "m",
        lazy.spawn("xrandr --output HDMI-0 --mode 1920x2400 --pos 5120x1500 --rotate right"),
        lazy.reload_config(),
        desc="Enable external monitor"
    ),
    # super-N → turn HDMI-0 off and reload config (falls back to one screen)
    Key(
        ["mod4"], "n",
        lazy.spawn("xrandr --output HDMI-0 --off"),
        lazy.reload_config(),
        desc="Disable external monitor"
    ),
]
