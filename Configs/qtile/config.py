from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook
from qtile_extras import widget as qtile_widgets

mod = "mod4"
terminal = guess_terminal()


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
# ---------------------------------------
#  _  _______   ____  __   _   ___  ___
# | |/ / __\ \ / /  \/  | /_\ | _ \/ __|
# | ' <| _| \ V /| |\/| |/ _ \|  _/\__ \
# |_|\_\___| |_| |_|  |_/_/ \_\_|  |___/
#
# ---------------------------------------


keys = [
    # -------------------------
    # CHANGING FOCUS OF WINDOWS
    # -------------------------
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),

    # ---------------------
    # SHUFFLING THE WINDOWS
    # ---------------------
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),


    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),

    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),

    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),

    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),


    # ---------------------
    # CUSTOM KEYBINDINGS
    # ---------------------
    Key(
        [mod], "r",
        lazy.spawn("/home/fakepickle/.config/rofi/scripts/launcher_t2"),
        desc="Spawn a command using a prompt widget"
    ),
    Key([mod, "shift"], "s",
        lazy.spawn("/home/fakepickle/.config/rofi/applets/bin/screenshot.sh"),
        desc="Take a screenshot"
        ),
    Key([], "XF86AudioPlay",
        lazy.spawn("/home/fakepickle/.config/qtile/scripts/volume.sh\
                    play_pause"),
        desc="Play/Pause"
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Next"
        ),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Previous"
        ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("/home/fakepickle/.config/qtile/scripts/volume.sh\
                    volume_up"),
        desc="Volume Up"
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("/home/fakepickle/.config/qtile/scripts/volume.sh\
                    volume_down"),
        desc="Volume Down"
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("/home/fakepickle/.config/qtile/scripts/volume.sh\
                    volume_mute"),
        desc="Volume mute"),
    Key([mod], "l",
        lazy.spawn("betterlockscreen -l"),
        desc="Locking laptop"),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("/home/fakepickle/.config/qtile/scripts/brightness.sh\
                    brightness_up"),
        desc="Brightness Up"
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("/home/fakepickle/.config/qtile/scripts/brightness.sh\
                    brightness_down"),
        desc="Brightness Down"
        ),
    ]


# ----------------------------------------------
# THIS IS FOR SHIFTING BETWEEN VIRTUAL TERMINALS
# ----------------------------------------------
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


# -----------------------------
# SETTING UP GROUPS FOR THE BAR
# -----------------------------
groups = [
    Group("1", label="\uf120", matches=[Match(wm_class="alacritty")]),
    Group("2", label="\uf268", matches=[Match(wm_class="google-chrome")]),
    Group("3", label="\uf07b", matches=[Match(wm_class="thunar")]),
    Group("4", label="\ue70c", matches=[Match(wm_class="code")]),
    Group("5", label="\uf1bc", matches=[Match(wm_class="spotify")]),
    Group("6", label="\uf121", matches=[Match(wm_class="discord")]),
]

# ---------------------
# SETTING UP WORKSPACES
# ---------------------
for i in groups:
    keys.extend([

        # SHIFTING BETWEEN WORKSPACES
        Key(
            [mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc=f"Switch to group {i}"
        ),

        # SHIFTING APP TO THAT WORKSPACE
        Key(
            [mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc=f"Switch to & move focused window to group {i}"
        ),
    ])


# ------------------------------
# SETTING UP LAYOUTS FOR THE BAR
# ------------------------------
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),

]

# ------------------------------
# SETTING UP DEFAULTS OF WIDGETS
# ------------------------------
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# ----------------------
# SETTING UP THE TOP BAR
# ----------------------
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.Image(
                    filename="/home/fakepickle/.config/qtile/Assets/linux.png",
                    margin=-5,
                    scale=True,
                    mouse_callbacks={"Button1":
                                     lambda:
                                     qtile.cmd_spawn("betterlockscreen -l")},
                    ),
                widget.Spacer(),
                widget.GroupBox(
                    highlight_color=["#000000", "#06402B"],
                    active="#ffffff",
                    inactive="#000000",
                    highlight_method="line",
                    fontsize=48,
                    padding=10,
                    font="CaskaydiaCove Nerd Font Mono",
                    disable_drag=True,
                    ),
                widget.Spacer(),
                widget.CPU(
                    fontsize=24,
                    font="CaskaydiaCove Nerd Font Mono",
                    format="{load_percent}%",
                    ),
                widget.Spacer(length=10),
                widget.DF(
                    fontsize=24,
                    font="CaskaydiaCove Nerd Font Mono",
                    format="{r:.2f}%",
                    visible_on_warn=False,
                    ),
                widget.Spacer(length=10),
                widget.Memory(
                    fontsize=24,
                    font="CaskaydiaCove Nerd Font Mono",
                    format="{MemUsed:.2f} MiB",
                    ),
                widget.Spacer(length=10),
                qtile_widgets.WiFiIcon(
                    interface="wlp4s0",
                    format="{essid}",
                    padding=10,
                    fontsize=24,
                    font="CaskaydiaCove Nerd Font Mono",
                    ),
                widget.Spacer(length=10),
                qtile_widgets.UPowerWidget(
                    battery_height=20,
                    battery_width=40,
                    border_charge_colour="#000000",
                    border_colour="#FF0000",
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize=24,
                    text_charging="{percentage: .0f}%"
                    ),
                widget.Spacer(length=10),
                widget.Clock(
                    format="%I:%M %p",
                    fontsize=24,
                    font="CaskaydiaCove Nerd Font Mono",
                    ),
                widget.Spacer(length=10),
                ],
            56,
            opacity=0.7,
            background="#00000000",
            margin=[10, 10, 10, 10],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.Image(
                    filename="/home/fakepickle/.config/qtile/Assets/linux.png",
                    margin=-5,
                    scale=True,
                    mouse_callbacks={"Button1":
                                     lambda:
                                     qtile.cmd_spawn("betterlockscreen -l")},
                    ),
                widget.Spacer(),
                widget.GroupBox(
                    highlight_color=["#000000", "#06402B"],
                    active="#ffffff",
                    inactive="#000000",
                    highlight_method="line",
                    fontsize=36,
                    padding=10,
                    font="CaskaydiaCove Nerd Font Mono",
                    disable_drag=True,
                    ),
                widget.Spacer(),
                widget.CPU(
                    fontsize=16,
                    font="CaskaydiaCove Nerd Font Mono",
                    format="{load_percent}%",
                    ),
                widget.Spacer(length=10),
                widget.DF(
                    fontsize=16,
                    font="CaskaydiaCove Nerd Font Mono",
                    format="{r:.2f}%",
                    visible_on_warn=False,
                    ),
                widget.Spacer(length=10),
                widget.Memory(
                    fontsize=16,
                    font="CaskaydiaCove Nerd Font Mono",
                    format="{MemUsed:.2f} MiB",
                    ),
                widget.Spacer(length=10),
                qtile_widgets.WiFiIcon(
                    interface="wlp4s0",
                    format="{essid}",
                    padding=7,
                    fontsize=16,
                    font="CaskaydiaCove Nerd Font Mono",
                    ),
                widget.Spacer(length=10),
                qtile_widgets.UPowerWidget(
                    battery_height=12,
                    battery_width=25,
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize=16,
                    text_charging="{percentage: .0f}%",
                    border_charge_colour="#000000",
                    border_colour="#FF0000",
                    ),
                widget.Spacer(length=10),
                widget.Clock(
                    format="%I:%M %p",
                    fontsize=16,
                    font="CaskaydiaCove Nerd Font Mono",
                    ),
                widget.Spacer(length=10),
                ],
            36,
            opacity=0.7,
            background="#00000000",
            margin=[10, 10, 10, 10],
        ),
    ),
]

# ----------------------
# FLOATING LAYOUTS SETUP
# ----------------------
mouse = [
    Drag([mod], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()
         ),
    Drag([mod], "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()
         ),
    Click([mod], "Button2",
          lazy.window.bring_to_front()
          ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
