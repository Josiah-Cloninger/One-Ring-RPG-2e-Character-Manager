from character2 import Character2, save_character, load_character
from calling2 import Callings2
from culture2 import Cultures2
from gear2 import Weapons2, Armours2, Headgears2, Shields2


input_str = "strength: 5, heart: 7, wits: 2"

attributes_list = input_str.split(", ")

attributes_dict = {}

for attribute in attributes_list:
    attribute_name, attribute_value = attribute.split(": ")
    attributes_dict[attribute_name] = int(attribute_value)

print(attributes_dict)