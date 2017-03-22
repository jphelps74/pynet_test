#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
import yaml

yaml_file = 'device.yml'
with open(yaml_file) as f:
    output = yaml.load(f)
    print output

    pynet_sw1 = (output)
    print pynet_sw1

#    vlans = [
#        'vlan 123',
#        'name jarrod',
#    ]
#
    net_connect2 = ConnectHandler(**pynet_sw1)
#    print net_connect2.send_config_set(vlans)
    print net_connect2.send_command("show vlan")
#    print net_connect2.send_config_from_file("vlan.txt")
#    print net_connect2.send_command("show vlan")
