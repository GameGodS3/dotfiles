# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
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

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

import os
import subprocess


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


mod = "mod4"
#mod = "mod1"
vol_up = "XF86AudioRaiseVolume"
vol_down = "XF86AudioLowerVolume"

keys = [
    Key(
        [mod], "Print",
        lazy.spawn(
            ["sh", "-c", "maim --format png /dev/stdout | xclip -selection clipboard -t image/png -i"])
    ),
    # Volume Controls
    Key(
        [mod], vol_up,
        lazy.spawn("amixer -q sset Master 2%+")
    ),
    Key(
        [mod], vol_down,
        lazy.spawn("amixer -q sset Master 2%-")
    ),
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    # Key([mod], "Return", lazy.spawn("st -f 'FiraMono Nerd Font-10'")),
    Key([mod], "Return", lazy.spawn("kitty")),
    #    Key([mod], "Return", lazy.spawn("gnome-terminal")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    #Key([mod], "r", lazy.spawncmd()),
    #Key([mod], "r", lazy.spawn("rofi -show run")),
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key([mod, "shift"], "r", lazy.spawncmd()),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "AD69AF",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='FiraMono Nerd Font',
    fontsize=12,
    padding=2,
    background='0f041a'
)

#arrow_colors = ['9B24A8', '3007C8']
arrow_colors = ['1E074F', '3A0E6E']

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                # widget.TextBox("default config", name="default"),
                widget.Systray(),

                widget.TextBox("🢐", fontsize=56,
                               foreground=arrow_colors[0],
                               padding=-3),
                widget.CurrentLayout(background=arrow_colors[0]),

                widget.TextBox("🢐", fontsize=56,
                               foreground=arrow_colors[1],
                               background=arrow_colors[0],
                               padding=-3),
                widget.Net(interface="wlp2s0", background=arrow_colors[1]),


                widget.TextBox("🢐", fontsize=56,
                               foreground=arrow_colors[1],
                               background=arrow_colors[0],
                               padding=-3),
                # widget.Volume(volume_down_command="amixer -q sset Master 2%-",
                #               volume_up_command="amixer -q sset Master 2%+"),
                widget.Volume(background=arrow_colors[1]),

                widget.TextBox("🢐", fontsize=56,
                               foreground=arrow_colors[0],
                               background=arrow_colors[1],
                               padding=-3),
                widget.TextBox("", font="Font Awesome 5 Free Solid",
                               background=arrow_colors[0]),
                widget.Clock(format='%d/%m/%Y %A %I:%M %p',
                             background=arrow_colors[0]),

                widget.TextBox("🢐", fontsize=56,
                               foreground=arrow_colors[1],
                               background=arrow_colors[0],
                               padding=-3),
                #                widget.BatteryIcon(background=arrow_colors[1]),
                widget.TextBox("", font="Font Awesome 5 Free Solid",
                               background=arrow_colors[1]),
                widget.Battery(background=arrow_colors[1], update_interval=10,
                               charge_char="", empty_char="", discharge_char="", full_char=""),

            ],
            30,
        ),
    ),
]

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
extentions = []

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
