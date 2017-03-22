#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
import yaml

yaml_file = 'device.yml'
with open(yaml_file) as f:
    output = yaml.load(f)
    pynet_sw1 = (output)
    net_connect2 = ConnectHandler(**pynet_sw1)
    print net_connect2.send_command("show vlan")
