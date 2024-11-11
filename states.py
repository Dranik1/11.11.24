import json
with open('states.json') as f:
    data=json.load(f)

for state in data['states']:
    print(state['name'], state['abbriviation'])

for state in data['states']:
    del state['area_codes']

with open('new_states', 'w') as f:
    json.dump(data, f, indent=4)

for a in data['states']:
    if a['name'][0]=="A":
        print(a['name'])
    else:
        pass 
