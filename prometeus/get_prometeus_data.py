#!/usr/bin/python3
import xml.etree.ElementTree as ET
import re

tree = ET.parse(r'prometeus/rocket.ork')
# tree = ET.parse("/home/rnduser/project-prometeus/prometeus/rocket.ork")
root = tree.getroot()


new_line = f'\n------------------------\n'
new_subline = f'***************************'


with open("prometeus_data.txt", "w") as file:
	file.write(new_line)
	for rocket in root.findall('rocket'):
		rocket_name = rocket.find('name').text  # Get Rocket Name
		designer_name = rocket.find('designer').text  # Get Designer Name
		file.write(f'Rocket Name: {rocket_name}\n')
		file.write(f'Designer Name: {designer_name}\n')

		# Find all Engine Configuration / 'TRUE' value point at the current active config
		all_configs = rocket.findall('motorconfiguration')
		file.write(f'{new_line}\n')
		for config in all_configs:
			file.write(f'Engine Configuration: {str(config.attrib.values())[14:-3]}\n')
		file.write(f'{new_line}')

	stages = rocket.findall('subcomponents/stage')
	for stage in stages:
		file.write(f'Number of stages: {len(stages)}\n')
		file.write(f'Stage Name: {stage.find("name").text}\n')

		regx = r'[<\/a-z>]'
		subcomponents = rocket.findall(f'subcomponents/stage/subcomponents/')

		for subcomponent in subcomponents:
			file.write(f'\tSubcomponent:\n')
			for attribute in subcomponent.iter():
				if not attribute.text:
						pass
				else:
					if "\n" not in attribute.text and attribute.text is not None:
						if attribute.text == "Trapezoidal fin set":
							break
						file.write(f'\t\t* {attribute.tag.capitalize()} -- {attribute.text}\n')
		
		parts = rocket.findall(f'subcomponents/stage/subcomponents/bodytube/subcomponents')
		for part in parts:
			file.write(f'\n\t\t\tParts:\n')
			for part_name in part.iter():
				if not part_name.text:
					pass
				else:
					if "\n" not in part_name.text and part_name.text is not None:
						if part_name.tag == 'name':
							file.write(f'\n')
							part_name.tag = f'Part {part_name.tag}'
						file.write(f'\t\t\t\t*{part_name.tag.capitalize()} -- {part_name.text}\n')
		file.write(new_line)

					



a = 5


# stages = root.find('rocket/subcomponents') # Get all stages
# file.write(f'Number of stages: {len(stages)}')

# for stage in stages: # Iterate through all stages
#     file.write(f'Stage Name: {root.find("rocket/subcomponents/stage/name").text}')
#     file.write(new_subline)

#     components = root.find('rocket/subcomponents/stage/subcomponents') # Get all components
#     file.write(f'\tNumber of components: {len(components)}')
#     for component in components: # Iterate through all components
#         component_name = root.find(f'rocket/subcomponents/stage/subcomponents/{component.tag}/name').text
#         file.write(f'\t\tComponent Name: {component_name}')
#         paints = root.find(f'rocket/subcomponents/stage/subcomponents/{component.tag}/appearance/paint')
#         file.write(f'\t\t\tAppearance:')
#         for paint in paints.items():
#             file.write(f'\t\t\t\t{paint[0].capitalize()} = {paint[1]}')
#         file.write(f'\t\t\t\tShine: {root.find(f"rocket/subcomponents/stage/subcomponents/{component.tag}/appearance/shine").text}')
#         file.write(f'\t\t\t\tFinish: {root.find(f"rocket/subcomponents/stage/subcomponents/{component.tag}/finish").text}')
#         file.write(f'\t\t\t\tMaterial: {root.find(f"rocket/subcomponents/stage/subcomponents/{component.tag}/material").text}')
#         file.write(f'\t\t{new_subline}')
