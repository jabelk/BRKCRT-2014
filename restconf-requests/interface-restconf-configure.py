import requests, json
base_path = "https://10.10.20.48:443"
url = base_path + "/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"
headers = {'content-type': 'application/yang-data+json','accept': 'application/yang-data+json'}
payload = json.dumps({"Cisco-IOS-XE-native:GigabitEthernet": {"name": "2","description": "Description updated by RESTCONF"}})
result = requests.patch(url, auth=("developer", "C1sco12345"),
                        headers=headers, verify=False, data=payload)
