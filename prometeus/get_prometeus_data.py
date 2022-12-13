#!/usr/bin/python3
import xml.etree.ElementTree as ET


tree = ET.parse("/home/rnduser/project-prometeus/prometeus/rocket.ork")
root = tree.getroot()

new_line = f'\n------------------------\n'
print(new_line)


for rocket in root.findall('rocket'):
    rocket_name = rocket.find('name').text # Get Rocket Name
    designer_name = rocket.find('designer').text # Get Designer Name
    print(f'Rocket Name: {rocket_name}')
    print(f'Designer Name: {designer_name}')

    all_configs = rocket.findall('motorconfiguration') # Find all Engine Configuration / 'TRUE' value point at the current active config
    print(new_line)
    for config in all_configs:
        print(f'Engine Configuration: {str(config.attrib.values())[14:-3]}')
    print(new_line)
    all_subcomponents = rocket.findall('subcomponents')
    for subcomponents in all_subcomponents:
	print(f'Subcomponents: {str(subcomponent.attrib.value())}')


