#!/usr/bin/python3
import xml.etree.ElementTree as ET


tree = ET.parse("/home/rnduser/project-prometeus/prometeus/rocket.ork")
root = tree.getroot()

#for child in root:
#    print(child.tag, child.attrib)
new_line = f'\n------------------------\n'
print(new_line)


for rocket in root.findall('rocket'):
    rocket_name = rocket.find('name').text
    designer_name = rocket.find('designer').text
    print(f'Rocket Name: {rocket_name}')
    print(f'Designer Name: {designer_name}')
    all_configs = rocket.findall('motorconfiguration')
    print(new_line)
    for config in all_configs:
        print(f'Engine Configuration: {str(config.attrib.values())[14:-3]}')
print(new_line)
