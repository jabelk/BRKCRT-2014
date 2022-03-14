# BRKCRT-2014

Jason:
We will need to work on slides 27-34. Here is what we need:

- Slide 28: Pick 3-4 topics from the ENAUTO blueprint to focus on. These tasks need to be related to the technical focus of the session. Let's pick a "Describe", a "Construct" and a "Troubleshoot"
- Slides 29-32: Based on the blueprint tasks that you will pick, we will need new questions. I can help you with that. Just give me the code and what it does.
- Slides 33-34: In this section we will have a live lab. Not something big, but we want to show how the exam questions we created above come hand-in-hand with the actual lab example.



These ones I think would be most interesting to me, not sure how many you are looking to cover, I can narrow down even more:
2.1 Identify the JSON instance based on a YANG model

2.2 Identify the XML instance based on a YANG model

2.3 Interpret a YANG module tree generated per RFC8340

2.4 Compare functionality, benefits, and uses of OpenConfig, IETF, and native YANG models

2.5 Compare functionality, benefits, and uses of NETCONF and RESTCONF

3.1 Implement device management and monitoring using NetMiko

3.2 Construct a Python script using ncclient that uses NETCONF to manage and monitor an IOS XE device

3.3 Configure device using RESTCONF API utilizing Python requests library

3.4 Utilize Ansible to configure an IOS XE device

## Details

Using [IOS XE on CSR Recommended Code](https://devnetsandbox.cisco.com/RM/Diagram/Index/05097c44-b162-4ea5-a1df-a449b4bd81c8)


curl -X 'GET' \
  'https://localhost:8443/restconf/proxy/https://10.10.20.48:443/restconf/data/ietf-routing:routing/routing-instance' \
  -H 'accept: application/yang-data+json'

https://localhost:8443/restconf/proxy/https://10.10.20.48:443/restconf/data/ietf-routing:routing/routing-instance

