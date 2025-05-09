#!/bin/bash

# Get the battery status and percentage using acpi -b
battery_status=$(acpi -b | grep -oP '(\d+:\d+):\d+ remaining')
battery_percentage=$(acpi -b | grep -oP '\d+(?=%)')

# If battery status is empty (charging or fully charged), set appropriate messages
if [ "$battery_percentage" -eq 80 ]; then
    battery_status="Battery is at 80%"
elif [ -z "$battery_status" ]; then
    battery_status="Battery is charging or fully charged"
fi

# Send a notification with notify-send
notify-send "Battery Status" "$battery_status"
