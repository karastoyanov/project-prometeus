#!/usr/bin/python3
import xml.etree.ElementTree as ET
import re

tree = ET.parse(r'prometeus/rocket.ork')
root = tree.getroot()


new_line = f'\n------------------------\n'
new_subline = f'***************************'


with open("prometeus_data.txt", "w") as file:
	file.write(new_line)
	for rocket in root.findall('rocket'):
		rocket_name = rocket.find('name').text  # Get Rocket Name
		designer_name = rocket.find('designer').text  # Get Designer Name
		print(f'Rocket Name: {rocket_name}\n')
		print(f'Designer Name: {designer_name}\n')
		file.write(f'Rocket Name: {rocket_name}\n')
		file.write(f'Designer Name: {designer_name}\n')

		# Find all Engine Configuration / 'TRUE' value point at the current active config
		all_configs = rocket.findall('motorconfiguration')
		print(f'{new_line}\n')
		file.write(f'{new_line}\n')
		for config in all_configs:
			print(f'Engine Configuration: {str(config.attrib.values())[14:-3]}\n')
			file.write(f'Engine Configuration: {str(config.attrib.values())[14:-3]}\n')
		print(f'{new_line}')
		file.write(f'{new_line}')

	stages = rocket.findall('subcomponents/stage')
	for stage in stages:
		print(f'Number of stages: {len(stages)}\n')
		print(f'Stage Name: {stage.find("name").text}\n')
		file.write(f'Number of stages: {len(stages)}\n')
		file.write(f'Stage Name: {stage.find("name").text}\n')

		regx = r'[<\/a-z>]'
		subcomponents = rocket.findall(f'subcomponents/stage/subcomponents/')

		for subcomponent in subcomponents:
			print(f'\tSubcomponent:\n')
			file.write(f'\tSubcomponent:\n')
			for attribute in subcomponent.iter():
				if not attribute.text:
						pass
				else:
					if "\n" not in attribute.text and attribute.text is not None:
						if attribute.text == "Trapezoidal fin set":
							break
						print(f'\t\t* {attribute.tag.capitalize()} -- {attribute.text}\n')
						file.write(f'\t\t* {attribute.tag.capitalize()} -- {attribute.text}\n')
		
		parts = rocket.findall(f'subcomponents/stage/subcomponents/bodytube/subcomponents')
		for part in parts:
			print(f'\n\t\t\tParts:\n')
			file.write(f'\n\t\t\tParts:\n')
			for part_name in part.iter():
				if not part_name.text:
					pass
				else:
					if "\n" not in part_name.text and part_name.text is not None:
						if part_name.tag == 'name':
							print(f'\n')
							file.write(f'\n')
							part_name.tag = f'Part {part_name.tag}'
						print(f'\t\t\t\t*{part_name.tag.capitalize()} -- {part_name.text}')
						file.write(f'\t\t\t\t*{part_name.tag.capitalize()} -- {part_name.text}\n')
		print(new_line)
		file.write(new_line)

