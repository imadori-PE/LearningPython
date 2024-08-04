import xml.etree.ElementTree as ET  
data = '''
<person>
    <name>Junior</name>
    <phone type="intl">
    +51 9** *** *56
    </phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print(f'Name: {tree.find('name').text}')
print(f'Attr: {tree.find('email').get('hide')}')