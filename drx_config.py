from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.command import lazy


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active="66ff66", inactive="006600",
                    this_current_screen_border="66ff66", this_screen_border="006600", other_screen_border="004400"
                ),
                widget.TextBox(text="/ win:"),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
            ],
            30,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active="66ff66", inactive="006600",
                    this_current_screen_border="66ff66", this_screen_border="006600", other_screen_border="004400"
                ),
                widget.TextBox(text="/ net:"),
                widget.Net(interface="eth2"),
                widget.TextBox(text="/ win:"),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
            ],
            30,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active="66ff66", inactive="006600",
                    this_current_screen_border="66ff66", this_screen_border="006600", other_screen_border="004400"
                ),
                widget.TextBox(text="/ mem:"),
                widget.Memory(),
                widget.TextBox(text="/ disk:"),
                widget.DF(visible_on_warn=False, format="{f}{m}/{s}{m}"),
                widget.TextBox(text="/ win:"),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
            ],
            30,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active="66ff66", inactive="006600",
                    this_current_screen_border="66ff66", this_screen_border="006600", other_screen_border="004400"
                ),
                widget.TextBox(text="/ cpu:"),
                widget.CPUGraph(
                    border_color="006600",
                    fill_color="66ff66",
                    graph_color="66ff66"
                ),
                widget.TextBox(text="/ temp:"),
                widget.ThermalSensor(foreground="66ff66", tag_sensor="Physical id 0"),
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
    Key(["mod4"], "Return", lazy.spawn("termite")),

    Key(
        ["mod4"], "u",
        lazy.to_screen(0)
    ),
    Key(
        ["mod4"], "i",
        lazy.to_screen(1)
    ),
    Key(
        ["mod4"], "o",
        lazy.to_screen(2)
    ),
    Key(
        ["mod4"], "p",
        lazy.to_screen(3)
    ),
]
