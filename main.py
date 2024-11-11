
people_string:{
    "people":[
    {
    "name":"Anna",
    "phone":"23002007",
    "emails":["g@gmail.com", "a@gmail.com"]    
    }
        ]}


import json
data=json.load(people_string)
print(data)
print(data['people'])
