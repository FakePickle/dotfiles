from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook
import fontawesome as fa
from qtile_extras import widget

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

color = [
    "#1F1F1F", # Darkest Shadow
    "#2D2D2D", # Deep Charcoal
    "#333333", # Charcoal
    "#474747", # Dark Gray
    "#646464", # Midtone Gray
    "#7A7A7A", # Smoky Gray
    "#A0A0A0", # Light Gray
    "#4285F8", # Royal Blue
    "#000000", # Black
    "#6A6A6A", # inactive
    "#D3D3D3", # Active
    "#2E2E2E",
    "#2F2F2F",
    "#303030",
    "#313131",
    "#323232",
    "#363636",
]


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
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
   
    # ---------------------
    # SHUFFLING THE WINDOWS
    # ---------------------
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
   

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
                widget.Spacer(
                    length=8,
                    background=color[2],
                ),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),


    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5"), desc = "Volume Up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5"), desc = "Volume Down"),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc = "Volume mute"),
    Key([mod], "l", lazy.spawn("betterlockscreen -l"), desc="Locking laptop"),
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
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group('7'),
    Group('8'),
    Group('9')
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

    layout.Max(),
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
                widget.TextBox(
                    fa.icons["caret-right"],
                    fontsize=100,
                    foreground=color[0],
                    background=color[2],
                    padding=-15,
                ),
                widget.GroupBox(
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize=24,
                    borderwidth=3,
                    highlight_color=color[6],
                    highlight_method="block",
                    active=color[10],
                    this_screen_border=color[6],
                    this_current_screen_border=color[6],
                    other_screen_border=color[4],
                    other_current_screen_border=color[4],
                    block_highlight_text_color="#FFFFFF",
                    background=color[2],
                    inactive=color[9],
                    rounded=True,
                    disable_drag=True,
                ),
                widget.TextBox(
                    fa.icons["caret-right"],
                    fontsize=100,
                    foreground=color[2],
                    padding=-14,
                    background=color[3],
                ),
                widget.Prompt(
                ),
                widget.WindowName(
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize=15,
                    background=color[3],
                ),
                widget.Spacer(
                    length=-7,
                    background=color[3],
                ),
                widget.TextBox(
                    fa.icons['caret-left'],
                    fontsize=100,
                    padding=-14,
                    background=color[3],
                    foreground=color[16],
                ),
                widget.Image(
                    filename="/home/fakepickle/.config/qtile/Assets/memory.png",
                    background=color[16],
                ),
                widget.Memory(
                    background=color[16],
                    foreground="#FFFFFF",
                    format = '{MemUsed: .0f}{mm}',
                    font = "CaskaydiaCove Nerd Font Mono",
                    fontsize = 15,
                    update_interval=5,
                ),
                widget.Spacer(
                    length=8,
                    background=color[16],
                ),
                widget.TextBox(
                    fa.icons["caret-left"],
                    fontsize=100,
                    padding=-14,
                    foreground=color[14],
                    background=color[16],
                ),
                widget.TextBox(
                    " ",
                    fontsize=20,
                    foreground="#FFFFFF",
                    background=color[14],
                ),
                widget.CPU(
                    background=color[14],
                    format="{load_percent}%",
                    foreground="#FFFFFF",
                    fontsize=16,
                    font="CaskaydiaCove Nerd Font Mono",
                ),
                widget.TextBox(
                    fa.icons["caret-left"],
                    fontsize=100,
                    padding=-14,
                    foreground=color[1],
                    background=color[14],
                ),
                widget.WiFiIcon(
                    active_colour="#FFFFFF",
                    background=color[1],
                    font="CaskaydiaCove Nerd Font Mono",
                    inactive_colour=color[3],
                    interface="wlo1",
                    fontsize=15,
                ),
                widget.Spacer(
                    length=10,
                    background=color[1],
                ),
                widget.BatteryIcon(
                    theme_path="/home/fakepickle/.config/qtile/Assets/Battery",
                    background=color[1],
                    update_interval=0.000001
                ),
                widget.Battery(
                    font='CaskaydiaCove Nerd Font Mono',
                    background=color[1],
                    format = '{percent:2.0%}',
                    fontsize=13,
                ),
                widget.Spacer(
                    length=10,
                    background=color[1],
                ),
                widget.PulseVolume(
                    theme_path="/home/fakepickle/.config/qtile/Assets/Volume/",
                    background=color[1],
                    padding=0,
                ),
                widget.PulseVolume(
                    background=color[1],
                    padding=3,
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize=15,
                    limit_max_volume=True,
                ),
                widget.TextBox(
                    fa.icons["caret-left"],
                    background=color[12],
                    foreground=color[0],
                    fontsize=100,
                    padding=-14,
                ),
                widget.Clock(
                    format = "%A %d %B %Y | %H:%M",
                    background=color[0],
                    fontsize=15,
                    font="CaskaydiaCove Nerd Font Mono",
                    padding=10,
                )
            ],
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [6,15,6,15],
        ),
    ),
]


# ----------------------
# FLOATING LAYOUTS SETUP
# ----------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
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
