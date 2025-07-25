from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.lazy import lazy

num_stacks = 2

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(active="66ff66", inactive="006600"),
                widget.TextBox(text="/ net:"),
                widget.Net(interface="enp0s31f6"),
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
                widget.ThermalSensor(foreground="66ff66", tag_sensor="Package id 0"),
                widget.TextBox(text="/ win:"),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
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
