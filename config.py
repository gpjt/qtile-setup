# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2016 Giles Thomas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile.config import Key, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, hook


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([script])


mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "j",
        lazy.layout.down()
    ),
    Key(
        [mod], "k",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "h",
        lazy.layout.previous()
    ),
    Key(
        [mod], "l",
        lazy.layout.next()
    ),

    # Move current window to between stacks
    Key(
        [mod, "control"], "h",
        lazy.layout.client_to_previous()
    ),
    Key(
        [mod, "control"], "l",
        lazy.layout.client_to_next()
    ),

    # Add/delete stacks
    Key(
        [mod], "i",
        lazy.layout.add()
    ),
    Key(
        [mod], "o",
        lazy.layout.delete()
    ),

    # Rotate panes of split stack
    Key(
        [mod], "Tab",
        lazy.layout.rotate()
    ),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod], "minus",
        lazy.layout.toggle_split()
    ),

    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout()),

    # Session management
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Start a terminal
    Key([mod], "Return", lazy.spawn("gnome-terminal")),

    # Mod-r to start a program
    Key([mod], "r", lazy.spawncmd()),

    # Mod-w to kill window
    Key([mod], "w", lazy.window.kill()),

    # Mod-control-k to lock screen
    Key([mod, "control"], "k", lazy.spawn("gnome-screensaver-command -l")),

]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + control + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "control"], i.name, lazy.window.togroup(i.name))
    )

layouts = [
    layout.Stack(border_focus="006600", num_stacks=2),
    layout.Max(),
    layout.TreeTab(
        font='DejaVu Sans Mono',
        panel_width=300, 
        inactive_bg="000000",
        inactive_fg="006600",
        active_bg="000000",
        active_fg="66ff66",
        sections=[""],
        section_fg="000000",
    ),
]

widget_defaults = dict(
    font='DejaVu Sans Mono',
    foreground="66ff66",
    fontsize=16,
    padding=3,
)

from local_config import screens, extra_keys
keys += extra_keys


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
