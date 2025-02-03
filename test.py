from character import Character, save_character, load_character
from ui_functions import weapon_names, select_character_to_load
from calling import Callings
from culture import Cultures
from gear import Weapons, Armours, Headgears, Shields
from standard_of_living import Standards_Of_Living

character_1 = load_character("dervorin")

new_favoured_skills = []

for skill in character_1.favoured_skills:
    new_favoured_skills.append(skill)

print(character_1.favoured_skills[0][0])
print(character_1.favoured_skills[0][1][0])
print(character_1.favoured_skills[0][1][1])