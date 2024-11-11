import json
people_string={"people":[{
    "name":"Anna",
    "phone":"23002007",
    "emails":["g@gmail.com", "a@gmail.com"]    
    }
        ]}



data=json.load(people_string)
print(data)
print(data['people'])
