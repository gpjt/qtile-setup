from libqtile.config import Screen
from libqtile import bar, widget

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(active="66ff66", inactive="006600"),
                widget.TextBox(text="/ net:"),
                widget.Net(interface="wlan0"),
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

extra_keys = []
