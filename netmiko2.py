#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'pyclass',
        'password': '88newclass',
    }

    vlans = [
        'vlan 123',
        'name jarrod',
    ]

    net_connect2 = ConnectHandler(**pynet_sw1)
    print net_connect2.send_config_set(vlans)
    print net_connect2.send_command("show vlan")
    print net_connect2.send_config_from_file("vlan.txt")
    print net_connect2.send_command("show vlan")
