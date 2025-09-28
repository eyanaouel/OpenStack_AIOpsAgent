#!/usr/bin/env python3
import json
import openstack
import os

def get_openstack_inventory():
    try:
        conn = openstack.connect(cloud=os.getenv("OS_CLOUD", "openstack"))
        servers = list(conn.compute.servers())
        
        inventory = {
            '_meta': {'hostvars': {}},
            'all': {'children': ['openstack']},
            'openstack': {'hosts': []}
        }
        
        for server in servers:
            if server.status == 'ACTIVE':
                # Récupérer la première IP disponible
                ip = None
                for network_name, addresses in (server.addresses or {}).items():
                    for addr in addresses:
                        if addr.get('addr'):
                            ip = addr['addr']
                            break
                    if ip:
                        break
                
                if ip:
                    inventory['openstack']['hosts'].append(server.name)
                    inventory['_meta']['hostvars'][server.name] = {
                        'ansible_host': ip,
                        'openstack_id': server.id,
                        'openstack_status': server.status,
                        'ansible_user': 'ubuntu'  # Ajustez selon vos images
                    }
        
        return inventory
        
    except Exception as e:
        return {'all': {'hosts': []}, '_meta': {'hostvars': {}}}

if __name__ == '__main__':
    print(json.dumps(get_openstack_inventory(), indent=2))
