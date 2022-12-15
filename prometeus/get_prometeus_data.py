#!/usr/bin/python3
import xml.etree.ElementTree as ET
import re

tree = ET.parse(r'prometeus/rocket.ork')
# tree = ET.parse("/home/rnduser/project-prometeus/prometeus/rocket.ork")
root = tree.getroot()


new_line = f'\n------------------------\n'
new_subline = f'***************************'
print(new_line)


for rocket in root.findall('rocket'):
    rocket_name = rocket.find('name').text  # Get Rocket Name
    designer_name = rocket.find('designer').text  # Get Designer Name
    print(f'Rocket Name: {rocket_name}')
    print(f'Designer Name: {designer_name}')

    # Find all Engine Configuration / 'TRUE' value point at the current active config
    all_configs = rocket.findall('motorconfiguration')
    print(new_line)
    for config in all_configs:
        print(f'Engine Configuration: {str(config.attrib.values())[14:-3]}')
    print(new_line)

stages = rocket.findall('subcomponents/stage')
for stage in stages:
	print(f'Number of stages: {len(stages)}')
	print(f'Stage Name: {stage.find("name").text}')

	regx = r'[<\/a-z>]'
	subcomponents = rocket.findall(f'subcomponents/stage/subcomponents/')

	for subcomponent in subcomponents:
			print(f'\tSubcomponent')
			for attribute in subcomponent.iter():
				if not attribute.text:
						pass
				else:
					if "\n" not in attribute.text and attribute.text is not None:
						if attribute.text == "Trapezoidal fin set":
							break
						print(f'\t{attribute.tag.capitalize()} -- {attribute.text}')
			print(new_line)

					



a = 5


# stages = root.find('rocket/subcomponents') # Get all stages
# print(f'Number of stages: {len(stages)}')

# for stage in stages: # Iterate through all stages
#     print(f'Stage Name: {root.find("rocket/subcomponents/stage/name").text}')
#     print(new_subline)

#     components = root.find('rocket/subcomponents/stage/subcomponents') # Get all components
#     print(f'\tNumber of components: {len(components)}')
#     for component in components: # Iterate through all components
#         component_name = root.find(f'rocket/subcomponents/stage/subcomponents/{component.tag}/name').text
#         print(f'\t\tComponent Name: {component_name}')
#         paints = root.find(f'rocket/subcomponents/stage/subcomponents/{component.tag}/appearance/paint')
#         print(f'\t\t\tAppearance:')
#         for paint in paints.items():
#             print(f'\t\t\t\t{paint[0].capitalize()} = {paint[1]}')
#         print(f'\t\t\t\tShine: {root.find(f"rocket/subcomponents/stage/subcomponents/{component.tag}/appearance/shine").text}')
#         print(f'\t\t\t\tFinish: {root.find(f"rocket/subcomponents/stage/subcomponents/{component.tag}/finish").text}')
#         print(f'\t\t\t\tMaterial: {root.find(f"rocket/subcomponents/stage/subcomponents/{component.tag}/material").text}')
#         print(f'\t\t{new_subline}')
