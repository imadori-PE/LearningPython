import json
data ='''
{
"name" : "Chuck",
"phone" : {
    "type" : "intl",
    "number": "+1 734 303 4556"
    },
    "email" : {
        "hide":"yes"
    }
}
'''
info = json.loads(data) # * return dictionary python
print('Name', info['name'])
print('Hide', info['email'])