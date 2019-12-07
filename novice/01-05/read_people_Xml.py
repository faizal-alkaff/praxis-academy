import xml.etree.ElementTree as ET

tree = ET.parse('data_people.xml')
root = tree.getroot()

for name in root.iter('name'):
    print('Nama :', name.text)
print('')
for website in root.iter('website'):
    print('Website :', website.text)
print('')
for city in root.iter('city'):
    print('City :', city.text)