# credit: https://github.com/CiscoDevNet/restconf-examples/blob/master/restconf-103/interfaceStatus.py
# path: https://10.10.20.48:443/restconf/data/ietf-routing:routing/routing-instance
"""
sample output:
(brkcrt) BRKCRT-2014$ python routing-restconf.py
{
  "ietf-routing:routing-instance": [
    {
      "name": "default",
      "description": "default-vrf [read-only]",
      "routing-protocols": {
        "routing-protocol": [
          {
            "type": "ietf-routing:static",
            "name": "1",
            "static-routes": {
              "ietf-ipv4-unicast-routing:ipv4": {
                "route": [
                  {
                    "destination-prefix": "0.0.0.0/0",
                    "next-hop": {
                      "outgoing-interface": "GigabitEthernet1"
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  ]
}

(brkcrt) BRKCRT-2014$
"""

import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

URL = "https://10.10.20.48:443"
USER = 'developer'
PASS = 'C1sco12345'

#api call to get information of all interfaces on the router
url = URL + "/restconf/data/ietf-routing:routing/routing-instance"
headers = {'content-type': 'application/yang-data+json',
           'accept': 'application/yang-data+json'}
result = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
print (result.text)

