from character import Character, save_character, load_character
from ui_functions import weapon_names, select_character_to_load
from calling import Callings
from culture import Cultures
from gear import Weapons, Armours, Headgears, Shields
from standard_of_living import Standards_Of_Living

value = "Bow "
active_character = select_character_to_load()
print(Weapons.by_name(value))