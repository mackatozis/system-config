#!/bin/env python

'''
This script is used to output the battery level of any Razer Device supported by the OpenRazer daemon.
'''

import argparse

from openrazer.client import DeviceManager

STATUS_DICT = {
    'Charging . . .': "\U0001F50C",
    'On battery': "\U0001F50B",
    'Disconnected': "\U0000274C"
}

DEVICE_TYPE = {
    'keyboard' : "\U0001F5AE",
    'mouse' : "\U0001F5B1",
    'mousemat' : None,
    'core' : None,
    'keypad' : None,
    'headset' : "\U0001F3A7",
    'accessory' : None
}

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()

# Helper function to recognize boolean arguments
def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('true', 't'):
        return True
    elif value.lower() in ('false', 'f'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected')

# Parser for command-line options
args_parser = argparse.ArgumentParser('Script for retrieving battery information of Razer devices')
required_arguments = args_parser.add_argument_group(title='Required Arguments')
required_arguments.add_argument("--info", "-i", nargs='?', default=False, type=str_to_bool, help="print device info", required=False)
required_arguments.add_argument("--type", "-t", help="device type", choices=['keyboard', 'mouse', 'mousemat', 'core', 'keypad', 'headset', 'accessory'], required=False)

parameters = vars(args_parser.parse_args())
is_info_enabled = parameters['info']
device_type = parameters['type']

# Iterate over each device
for device in device_manager.devices:
    
    if device_type is not None:
        if device_type != device.type:
            continue

    status = ''
    battery_level = device.battery_level;
    if device.is_charging:
        status = 'Charging . . .'
    else:
        if battery_level > 0:
            status = 'On battery'
        else:
            status = 'Disconnected'
            
    if is_info_enabled:
        print ("{}\nStatus: {} {}".format(device.name, STATUS_DICT[status], status))
        exit()
        
    if device_type is not None and DEVICE_TYPE[device_type] is not None and status != 'Disconnected':
        print ("{} {}%".format(DEVICE_TYPE[device_type], battery_level))
    else:
        print ("{} {}%".format(STATUS_DICT[status], battery_level))
