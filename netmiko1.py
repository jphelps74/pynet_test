#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password':  '88newclass',
    }
    
    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'pyclass',
        'password': '88newclass',
    }

    net_connect1 = ConnectHandler(**pynet_rtr1)
    print net_connect1.find_prompt()
    print net_connect1.send_command("show run")
    print net_connect1.send_command("show ver")
    net_connect2 = ConnectHandler(**pynet_sw1)
    print net_connect2.find_prompt()
    print net_connect2.send_command("show run")
    print net_connect2.send_command("show ver")
