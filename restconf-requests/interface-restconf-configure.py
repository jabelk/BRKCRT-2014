# credit: https://github.com/CiscoDevNet/restconf-examples/blob/master/restconf-103/interfaceStatus.py
# credit: https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/5eU6DfQV/LTRCRT-2700-LG.pdf

# path: https://10.10.20.48:443/restconf/data/ietf-routing:routing/routing-instance
"""
sample output:
(brkcrt) BRKCRT-2014$ python interface-restconf-configure.py
{
  "Cisco-IOS-XE-native:GigabitEthernet": {
    "name": "2",
    "description": "Network Interface",
    "shutdown": [null],
    "mop": {
      "enabled": false,
      "sysid": false
    },
    "Cisco-IOS-XE-ethernet:negotiation": {
      "auto": true
    }
  }
}


{
  "Cisco-IOS-XE-native:GigabitEthernet": {
    "name": "2",
    "description": "Description updated by RESTCONF",
    "shutdown": [null],
    "mop": {
      "enabled": false,
      "sysid": false
    },
    "Cisco-IOS-XE-ethernet:negotiation": {
      "auto": true
    }
  }
}

(brkcrt) BRKCRT-2014$
"""

import sys
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

URL = "https://10.10.20.48:443"
USER = 'developer'
PASS = 'C1sco12345'

#api call to get information of all interfaces on the router
url = URL + "/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
headers = {'content-type': 'application/yang-data+json',
           'accept': 'application/yang-data+json'}
result = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
print (result.text)

payload = json.dumps({
    "Cisco-IOS-XE-native:GigabitEthernet": {
        "name": "2",
        "description": "Description updated by RESTCONF"
    }
})
url = URL + "/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"
result = requests.patch(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)
print(result.text)

url = URL + "/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
result = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
print(result.text)
