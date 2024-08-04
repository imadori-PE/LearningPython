import xml.etree.ElementTree as ET  
data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Junior</name>
        </user>
        <user x="7">
            <id>007</id>
            <name>Miguel</name>
        </user>
    </users>
</stuff>
'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('User Count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))