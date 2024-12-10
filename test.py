from character2 import Character2, save_character, load_character
from calling2 import Callings2
from culture2 import Cultures2
from gear2 import Weapons2, Armours2, Headgears2, Shields2


active_character = Character2(
    culture=Cultures2.RANGER, 
    attribute_choice=4, 
    weapon_skill_levels={"swords": 2, "bows": 1, "spears": 0, "axes": 0}, 
    favoured_skill_choices=["lore'", "courtesy", "travel"], 
    distinctive_features=["swift", "honourable"], 
    name="Dervorin",
    age="24",
    calling=Callings2.MESSENGER,
    starting_virtue="Heir of Arnor",
    starting_reward="Keen Longsword"
    )

active_character.weapons.append(Weapons2.LONG_SWORD)
active_character.armour = Armours2.LEATHER_CORSLET
active_character.weapons[0].notes = "Piercing blow happens on a 9"

print(Headgears2.names())