import xml.etree.ElementTree as ET

# create the file structure
data = ET.Element('data')
people = ET.SubElement(data, 'people')
name1 = ET.SubElement(people, 'name')
website1 = ET.SubElement(people, 'website')
city1 = ET.SubElement(people, 'city')
name2 = ET.SubElement(people, 'name')
website2 = ET.SubElement(people, 'website')
city2 = ET.SubElement(people, 'city')
name3 = ET.SubElement(people, 'name')
website3 = ET.SubElement(people, 'website')
city3 = ET.SubElement(people, 'city')
name1.set('name','name1')
name2.set('name','name2')
name3.set('name','name3')
name1.text = 'Scott'
website1.text = 'stackabuse.com'
city1.text = 'Nebraska'
name2.text = 'Larry'
website2.text = 'google.com'
city2.text = 'Michigan'
name3.text = 'Tim'
website3.text = 'apple.com'
city3.text = 'Alabama'

#create a new XML file with the results
mydata = ET.tostring(data)
myfile = open("data_people.xml", "wb")
myfile.write(mydata)

#tree = ET.parse('data_people.xml')
#root = tree.getroot()
#
## changing a field text
#for elem in root.iter('item'):
#    elem.text = 'new text'
#
## modifying an attribute
#for elem in root.iter('item'):
#    elem.set('name', 'newitem')
#
## adding an attribute
#for elem in root.iter('item'):
#    elem.set('name2', 'newitem2')
#
#tree.write('data_people.xml')