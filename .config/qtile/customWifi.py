import iwlib

from libqtile.log_utils import logger
from libqtile.pangocffi import markup_escape_text
from libqtile.widget import base


def get_status(interface_name):
    interface = iwlib.get_iwconfig(interface_name)
    if "stats" not in interface:
        return None, None
    quality = interface["stats"]["quality"]
    essid = bytes(interface["ESSID"]).decode()
    return essid, quality

wifiIcons = {
    range(0, 20): "󰤯",  # Very weak signal
    range(20, 40): "󰤟",  # Weak signal
    range(40, 60): "󰤢",  # Medium signal
    range(60, 80): "󰤥",  # Strong signal
    range(80, 101): '󰤨', # Full
}

class Wlan(base.InLoopPollText):
    """
    Displays Wifi SSID and quality.

    Widget requirements: iwlib_.

    .. _iwlib: https://pypi.org/project/iwlib/
    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("interface", "wlan0", "The interface to monitor"),
        (
            "ethernet_interface",
            "eth0",
            "The ethernet interface to monitor, NOTE: If you do not have a wlan device in your system, ethernet functionality will not work, use the Net widget instead",
        ),
        ("update_interval", 1, "The update interval."),
        ("disconnected_message", "Disconnected", "String to show when the wlan is diconnected."),
        ("ethernet_message", "eth", "String to show when ethernet is being used"),
        (
            "use_ethernet",
            False,
            "Activate or deactivate checking for ethernet when no wlan connection is detected",
        ),
        (
            "format",
            "{essid} {quality}/70",
            'Display format. For percents you can use "{essid} {percent:2.0%}"',
        ),
        (
            "charset",
            "utf-8",
            "The character set to use for the text. "
        )
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Wlan.defaults)
        self.ethernetInterfaceNotFound = False

    def _get_icon(self, strength):
        """Return the appropriate WiFi icon based on signal strength."""
        strength *= 100
        if strength is None:
            return "󰤭"  # No signal icon
        for r in wifiIcons.keys():
            if int(strength) in r:
                return wifiIcons[r]
        return "󰤭"  # Default to no signal

    def poll(self):
        try:
            essid, quality = get_status(self.interface)
            if self.use_ethernet:
                try:
                    with open(
                        f"/sys/class/net/{self.ethernet_interface}/operstate"
                    ) as statfile:
                        if statfile.read().strip() == "up":
                            return self.ethernet_message
                        else:
                            return self.format.format(
                                essid=essid,
                                quality=quality,
                                icon=self._get_icon(quality/70),
                                percent=quality / 70,
                            )
                except FileNotFoundError:
                    if not self.ethernetInterfaceNotFound:
                        logger.error("Ethernet interface has not been found!")
                        self.ethernetInterfaceNotFound = True
                    return self.disconnected_message
            else:
                return self.disconnected_message
        except OSError:
            logger.error(
                "Probably your wlan device is switched off or "
                " otherwise not present in your system."
            )