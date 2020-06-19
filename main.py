import json


def get_json(filename):
    with open(filename) as f:
        return json.load(f)


patient = get_json('patient1.json')

resources = {}
encounter = 0
procedure = 0
for entry in patient['entry']:
    resource = entry['resource']
    resource_type = resource['resourceType']

    if resource_type not in resources.keys():
        resources[resource_type] = []

    with open(f'{str(resource_type).lower()}_{len(resources[resource_type])}.json', 'w') as enc:
        enc.write(json.dumps(resource))

    resources[resource_type].append(resource)

for key in resources.keys():
    print(f'{key}: {len(resources[key])}')
