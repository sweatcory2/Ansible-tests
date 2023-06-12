#!/usr/bin/env python3

# Task 2, Step 1 
from pprint import pprint
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Task 2, Step 2 - Build API call variables
NAUTOBOT_TOKEN = ' 63b28469eb66e2379344e383641c4f2b9dc14ce2'
DEVICES_API_URL = 'http://172.16.1.129:8000/api/dcim/devices/'
METHOD = 'GET'
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Token {NAUTOBOT_TOKEN}'
}
PARAMETERS = {
    'site': 'anstest'
}

# Task 2, Step 3 - Execute the API call
devices = requests.request(method=METHOD, url=DEVICES_API_URL, headers=HEADERS, params=PARAMETERS, verify=False)
devices_json = devices.json()
#pprint(devices_json)




#Task 2, Step 4 - Add hosts to hostvars
hostvars = {
    '_meta': {
        'hostvars': {}
    }
}

for device in devices_json['results']:
    hostvars['_meta']['hostvars'].update(
        {
            device['name']: {
            'ansible_host': device['primary_ip4']['address'].split('/')[0],
            'device_type': device['device_type']['model'],
            }
        }
    )
#pprint(hostvars)

# Task 2, Step 5 - Group hosts based on enclave
groups = {
    'all': {
        'children': []
    },
    'grey_devices': {
        'hosts': []
    },
    'black_devices': {
        'hosts': []
    },
    'routers': {
        'hosts': []
    },
    'switches': {
        'hosts': []
    }
}

# # Task 2, Steps 6 - Group hosts based device type

# Step 6 for device in hostvars['_meta']['hostvars'].keys():
for device in hostvars['_meta']['hostvars'].keys():
    if 'GREY' in device:
        groups['grey_devices']['hosts'].append(device)

    if 'BLACK' in device:
        groups['black_devices']['hosts'].append(device)

    if 'ROUTER' in device:
        groups['routers']['hosts'].append(device)

    if 'SWITCH' in device:
        groups['switches']['hosts'].append(device)

# Step 7
for group in groups.keys():
    if group != 'all':
        groups['all']['children'].append(group)
#pprint(groups)


# Task 2, Step 8 - Combine inventory components into one variable
inventory = {}
inventory.update(hostvars)
inventory.update(groups)
#pprint(inventory)


# Task 2, Step 9 - Print JSON inventory
print(json.dumps(inventory, indent=4))