# BRKCRT-2014

Using CSR XE on recommended code:
https://devnetsandbox.cisco.com/RM/Diagram/Index/cae403c2-27af-4c7d-b1e1-99b7d42f1504?diagramType=Topology 


## Sample Outputs

### Ansible

> ansible-galaxy collection install cisco.ios
```
(brkcrt) ansible$ ansible-playbook -i inventory.ini pb-configure-snmp.yaml -v
Using /etc/ansible/ansible.cfg as config file

PLAY [PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS] *********************************

TASK [TASK 1 in PLAY 1 - CONFIGURE SNMP LINES] ***************************************
[WARNING]: To ensure idempotency and correct diff the input configuration lines
should be similar to how they appear if present in the running configuration on
device
changed: [csr1] => {"banners": {}, "changed": true, "commands": ["snmp-server community belk-demo1 RO"], "updates": ["snmp-server community belk-demo1 RO"]}

TASK [TASK 2 in PLAY 1 - VERIFY SNMP LINES PRESENT] **********************************
ok: [csr1] => {"changed": false, "stdout": ["snmp-server community belk-demo RO\nsnmp-server community belk-demo1 RO\nsnmp-server location VEGAS\nsnmp-server contact JASON_BELK"], "stdout_lines": [["snmp-server community belk-demo RO", "snmp-server community belk-demo1 RO", "snmp-server location VEGAS", "snmp-server contact JASON_BELK"]]}

PLAY RECAP ***************************************************************************
csr1                       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

(brkcrt) ansible$
```

### restconf requests configure

extra lines that help
```
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

```

```
# credit: https://github.com/CiscoDevNet/restconf-examples/blob/master/restconf-103/interfaceStatus.py
# credit: https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/5eU6DfQV/LTRCRT-2700-LG.pdf

# path: https://10.10.20.48:443/restconf/data/ietf-routing:routing/routing-instance

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

```
