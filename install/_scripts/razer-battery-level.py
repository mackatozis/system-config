#!/bin/env python
from openrazer.client import DeviceManager

IS_CHARGING='🔌'
ON_BATTERY='🔋'
NOT_CONNECTED='❌'

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()

# Iterate over each device and print its battery level
for device in device_manager.devices:

    status = ''
    battery_level = device.battery_level;
    if device.is_charging:
        status = IS_CHARGING
    else:
        if battery_level > 0:
            status = ON_BATTERY
        else:
            status = NOT_CONNECTED
            print ("{}: {} not connected".format(device.name, status))
            exit()

    print ("{}: {} {}%".format(device.name, status, battery_level))
