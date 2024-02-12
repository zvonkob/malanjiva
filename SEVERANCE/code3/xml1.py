import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

person = ET.fromstring(data)

print('Name:', person.find('name').text)

print('Phone:', person.find('phone').text.strip())

print('Email:', person.find('email').text)
print('    Attr:', person.find('email').get('hide'))
