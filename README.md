# BRKCRT-2014

ansible-galaxy collection install cisco.ios


sample output Ansible
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