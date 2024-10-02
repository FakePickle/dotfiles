from libqtile import bar, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.layout.columns import Columns
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

    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating"
        ),

    Key([mod, "shift"], "s",
        lazy.spawn(os.path.expanduser("~/.config/rofi.backup/applets/bin/screenshot.sh")),
        desc="Toggle screenshot"
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
        lazy.spawn(os.path.expanduser("~/.config/rofi/scripts/launcher")),
        desc="Spawn a command using a prompt widget"
    ),
    Key(
        [mod, "shift"], "q",
        lazy.spawn(f"sh -c {os.path.expanduser("~/.config/rofi/scripts/power")}"),
        desc="Spawn powermenu"
    ),
    Key([], "XF86AudioPlay",
        lazy.spawn(f"{os.path.expanduser("~/.config/qtile/scripts/volume.sh")}\
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
        lazy.spawn(
            f"{os.path.expanduser("~/.config/qtile/scripts/volume.sh")}\
            volume_up"
        ),
        desc="Volume Up"
        ),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn(
            f"{os.path.expanduser("~/.config/qtile/scripts/volume.sh")}\
            volume_down"
        ),
        desc="Volume Down"
        ),

    Key([], "XF86AudioMute",
        lazy.spawn(
            f"{os.path.expanduser("~/.config/qtile/scripts/volume.sh")}\
            volume_mute"
        ),
        desc="Volume mute"),

    Key([mod], "l",
        lazy.spawn(
            f"i3lock -i {os.path.expanduser("~/Downloads/fog_forest_2.png")}"
        ),
        desc="Locking laptop"),

    Key([], "XF86MonBrightnessUp",
        lazy.spawn(
            f"{os.path.expanduser("~/.config/qtile/scripts/brightness.sh")}\
            brightness_up"
        ),
        desc="Brightness Up"
        ),

    Key([], "XF86MonBrightnessDown",
        lazy.spawn(
            f"{os.path.expanduser("~/.config/qtile/scripts/brightness.sh")}\
            brightness_down"
        ),
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
            lazy.core.change_vt(vt).when(
                func=lambda: qtile.core.name == "wayland"
            ),
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
    Group("6", label="\uf249", matches=[Match(wm_class="obsidian")]),
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
columns_layout = Columns(
    border_width=2,
    border_focus="#2E8B57",
    border_normal="#696969",
    margin=5,
)


# Adjust border and margin for a single window
def adjust_single_window_layout():
    for group in qtile.groups:
        windows = len(group.windows)
        if windows == 1:
            for layouts in group.layouts:
                layouts.border_width = 4  # Thicker border for single window
                layouts.margin = 12       # More padding for single window
        else:
            for layouts in group.layouts:
                layouts.border_width = 2  # Default border width
                layouts.margin = 12


# Hooks to adjust layout when windows are managed or killed
hook.subscribe.client_managed(adjust_single_window_layout)
hook.subscribe.client_killed(adjust_single_window_layout)

# Add layouts to your list
layouts = [
    columns_layout,
]

# ------------------------------
# SETTING UP DEFAULTS OF WIDGETS
# ------------------------------
widget_defaults = dict(
    font="Hack Nerd Font Mono",
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
                    filename=os.path.expanduser(
                        "~/.config/qtile/Assets/linux.png"
                    ),
                    margin=-5,
                    scale=True,
                    mouse_callbacks={
                        "Button1":
                        lambda:
                        qtile.spawn(
                                f"i3lock -i \
                                {os.path.expanduser("~/Downloads/fog_forest_2.png")}"
                            ),
                        "Button3":
                        lambda:
                        qtile.spawn(
                            "sh -c /home/fakepickle/.config/rofi/scripts/power"
                        )},
                    ),
                widget.Spacer(),
                widget.GroupBox(
                    highlight_color=["#000000", "#06402B"],
                    active="#ffffff",
                    inactive="#000000",
                    highlight_method="line",
                    fontsize=44,
                    padding=10,
                    font="Hack Nerd Font Mono",
                    disable_drag=True,
                    ),
                widget.Spacer(),
                widget.DF(
                    fontsize=22,
                    font="Hack Nerd Font Bold",
                    format="{r:.2f}% |",
                    visible_on_warn=False,
                    ),
                widget.Spacer(length=10),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=22,
                ),
                widget.Battery(
                    font="Hack Nerd Font Bold",
                    fontsize=22,
                    format='{percent:2.0%} |',
                ),
                widget.Spacer(10),
                qtile_widgets.WiFiIcon(
                    interface="wlp4s0",
                    format="{essid}",
                    fontsize=22,
                    font="Hack Nerd Font Bold",
                    ),
                widget.TextBox(
                    text=" |",
                    font="Hack Nerd Font Bold",
                    fontsize=22,
                ),
                widget.Spacer(length=10),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=22,
                    foreground='#FFFFFF',
                ),

                widget.Clock(
                    format='%I:%M %p',
                    foreground='#FFFFFF',
                    font="Hack Nerd Font Bold",
                    fontsize=22,
                ),

                widget.Spacer(length=10),
                ],
            36,
            opacity=0.7,
            background="#00000000",
            margin=[4, 10, 4, 10],
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

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
