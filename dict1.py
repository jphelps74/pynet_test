#!/usr/bin/env python
net_device = {
    'ip_addr':  '127.0.0.1',
    'username': 'admin',
    'password': 'pass',
    'vendor':   'juniper',
    'model':    'mx'
}
for element in net_device.items():
    print element
update_model = raw_input('Update Model: ')
net_device['model'] = update_model
for element in net_device.items():
    print element
net_device['secret'] = 'test123'
print net_device['secret']
print net_device.get('device_type', 'cisco_ios')

