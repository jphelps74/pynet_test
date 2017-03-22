#!/usr/bin/env python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from pynxos.device import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nexus_ip = "nxos1.twb-tech.com"
nxs_test = Device(host=nexus_ip, username="pyclass", password='88newclass',
                  transport='https', port=8443)

#my_facts = nxs_test.facts
#print my_facts
output = nxs_test.show("show version", raw_text=False)
proc = output['proc_board_id']
mem = output['memory']
print " proc_board_id: {}".format(proc)
print " memory: {}".format(mem)
