import json
input ='''
[
    {
        "id":"001",
        "x":"2",
        "name":"junior"
    },
    {
        "id":"002",
        "x":"5",
        "name":"miguel"
    }
]
'''
input2='["Glenn","Sally","Jen"]'

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

info = json.loads(input2)
print(type(info), info)