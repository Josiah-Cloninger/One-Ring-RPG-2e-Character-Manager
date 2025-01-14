import os

import questionary
from questionary import print

from culture import Cultures, Culture, all_combat_proficiencies
from character import Character
from calling import Calling, Callings
from gear import Weapons, Armours, Shields, Headgears


styles_print = {
    "culture": "#0001e0",
    "yellow": "#deea0b",
    "specialty": "#4fdb5a",
    "background": "#f78400",
    "white": "#ffffff"
}
styles_choice = questionary.Style([
    ('yellow', '#deea0b'),
    ('culture', '#0001e0'),
    ('specialty', '#4fdb5a'),
    ('background', '#f78400'),
    ('white', '#ffffff')
])


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    clear_console()
    questionary.print("The One Rings RPG Character Sheet\n", style=styles_print["yellow"])


def select_culture():
    title()
    questionary.print("Select Culture:\n", style=styles_print["yellow"])
    answer = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:culture", culture_name),
                ],
                value=culture_name
            ) for culture_name in Cultures.names()
        ],
        style=styles_choice
    ).ask()
    return Cultures.by_name(answer)


def select_attributes(selected_culture: Culture):
    title()
    culture_attributes = []
    enumerater = 0
    times_run = 0
    set_of_attributes = ""
    for a in selected_culture.attributes:
        for i in a:
            set_of_attributes += str(i)
            set_of_attributes += str(": ")
            set_of_attributes += str(selected_culture.attributes[enumerater][i])
            times_run += 1
            if times_run % 3 == 0:
                culture_attributes.append(set_of_attributes)
            else:
                set_of_attributes += ", "
        enumerater += 1
        set_of_attributes = ""
    questionary.print("Select Attributes:\n", style=styles_print["yellow"])
    answer = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", a)
                ],
                value=a
            ) for a in culture_attributes
        ],
        style=styles_choice
    ).ask()

    # generating the dictionary required by the __init__ function for the character class
    attributes_list = answer.split(", ")

    attributes_dict = {}

    for attribute in attributes_list:
        attribute_name, attribute_value = attribute.split(": ")
        attributes_dict[attribute_name] = int(attribute_value)

    return attributes_dict


def select_combat_proficiencies(selected_culture: Culture):
    title()
    
    # selecting one of the combat proficiencies indicated by your culture to start at level 2
    questionary.print("Select one of the following Combat Proficiencies to start at level 2:\n", style=styles_print["yellow"])
    level_2_choice = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", proficiency)
                
                ],
                value=proficiency
            )for proficiency in selected_culture.combat_proficiencies
        ],
        style=styles_choice
    ).ask()

    # selecting one of any combat proficiencies to start at level 1
    questionary.print("Select one of the following Combat Proficiencies to start at level 1:\n", style=styles_print["yellow"])
    level_1_choice = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", proficiency)
                
                ],
                value=proficiency
            )for proficiency in [x for x in all_combat_proficiencies if x != level_2_choice]
        ],
        style=styles_choice
    ).ask()

    # generating the dictionary required by the __init__ function for the character class
    combat_proficiencies = {"axes": 0, "bows": 0, "spears": 0, "swords": 0}

    combat_proficiencies.update({level_2_choice: 2})
    combat_proficiencies.update({level_1_choice: 1})

    return combat_proficiencies


def select_distinctive_features(selected_background):
    title()
    questionary.print("Select Distinctive Features:\n", style=styles_print["yellow"])
    selected_distinctive_features = questionary.checkbox(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", a)
                ],
                value=a
            ) for a in selected_background.distinctive_features
        ],
        style=styles_choice,
        validate=lambda answer: "Please select two distinctive features." if len(answer) != 2 else True
    ).ask()
    return selected_distinctive_features


def select_name():
    title()
    questionary.print("Enter Name:\n", style=styles_print["yellow"])
    selected_name = questionary.text(
        "",
        style=styles_choice
    ).ask()
    return selected_name


def select_age():
    title()
    questionary.print("Enter Age:\n", style=styles_print["yellow"])
    selected_age = questionary.text(
        "",
        style=styles_choice
    ).ask()
    return selected_age


def select_calling():
    title()
    questionary.print("Select Calling:\n", style=styles_print["yellow"])
    answer = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:calling", calling_name),
                ],
                value=calling_name
            ) for calling_name in Callings.names()
        ],
        style=styles_choice
    ).ask()
    return Callings.by_name(answer)


def select_favoured_skills(selected_culture: Culture,selected_calling: Calling):
    favoured_skills = []
    title()

    # selecting favoured skill from culture
    questionary.print("Select one favoured skill from you culture:\n", style=styles_print["yellow"])
    favoured_skills.append(questionary.select(
            "",
            choices=[
                questionary.Choice(
                    title=[
                        ("class:white", skill_name)
                    ],
                    value=skill_name
                ) for skill_name in selected_culture.favoured_skills
            ],
            style=styles_choice
        ).ask()
    )
    
    # selecting two favoured skills from calling
    questionary.print("Select two favoured skills from your calling:\n", style=styles_print["yellow"])
    favoured_skills.append(questionary.checkbox(
            "",
            choices=[
                questionary.Choice(
                    title=[
                        ("class:white", a)
                    ],
                    value=a
                ) for a in selected_calling.favoured_skills if a not in favoured_skills
            ],
            style=styles_choice,
            validate=lambda answer: "Please select two favoured skills." if len(answer) != 2 else True
        ).ask()
    )


def select_skill_upgrade(character: Character):
    title()
    questionary.print("Upgrade Common Skill:\n", style=styles_print["yellow"])
    answer = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", skill_name + ": " + str(skill_level))
                ],
                value=skill_name
            ) for skill_name, skill_level in character.skill_levels.items()
        ],
        style=styles_choice
    ).ask()
    return answer


def upgrade_skill(character: Character, skill: str, previous_experience_points: int):
    if previous_experience_points >= character.skill_levels[skill] + 1:
        character.skill_levels[skill] += 1
        previous_experience_points -= character.skill_levels[skill]
        return previous_experience_points
    else:
        print("You do not have enough experience to upgrade this skill.")
        return previous_experience_points


def select_weapon_skill_upgrade(character: Character):
    title()
    questionary.print("Upgrade Weapon Skill:\n", style=styles_print["yellow"])
    answer = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", skill_name + ": " + str(skill_level))
                ],
                value=skill_name
            ) for skill_name, skill_level in character.combat_proficiencies.items()
        ],
        style=styles_choice
    ).ask()
    return answer


def upgrade_weapon_skill(character: Character, skill: str, previous_experience_points: int):
    if previous_experience_points >= character.combat_proficiencies[skill] * 2 + 2:
        character.combat_proficiencies[skill] += 1
        previous_experience_points -= character.combat_proficiencies[skill] * 2
        return previous_experience_points
    else:
        print("You do not have enough experience to upgrade this skill.")
        return previous_experience_points


def previous_experience(character: Character):
    continue_loop = True
    previous_experience_points = 10
    while previous_experience_points > 0 and continue_loop:
        title()
        print("Skill Levels:\n", style=styles_print["yellow"])
        for skill, level in character.skill_levels.items():
            print(f"{skill}: {level}")
        print("\Combat Proficiency Levels:\n", style=styles_print["yellow"])
        for skill, level in character.combat_proficiencies.items():
            print(f"{skill}: {level}")
        print("\nPoints Remaining:\n", style=styles_print["yellow"])
        print(str(previous_experience_points))
        print("\n")
        answer = questionary.select(
            "",
            choices=[
                questionary.Choice(
                    title=[
                    ("class:white", o),
                    ],
                    value=o
                    )for o in ["Upgrade Skill", "Upgrade Combat Proficiency Skill", "Continue without spending remainding points"]
                ],
            style=styles_choice,
        ).ask()
        if answer == "Upgrade Skill":
            skill_to_upgrade = select_skill_upgrade(character)
            previous_experience_points = upgrade_skill(character, skill_to_upgrade, previous_experience_points)
        elif answer == "Upgrade Combat Proficiency Skill":
            weapon_skill_to_upgrade = select_weapon_skill_upgrade(character)
            previous_experience_points = upgrade_weapon_skill(character, weapon_skill_to_upgrade, previous_experience_points)
        elif answer == "Continue without spending remainding points":
            continue_loop = False


def select_virtue():
    title()
    questionary.print("Enter Virtue Name:\n", style=styles_print["yellow"])
    selected_virtue = questionary.text(
        "",
        style=styles_choice
    ).ask()
    return selected_virtue


def select_reward():
    title()
    questionary.print("Enter Reward Name:\n", style=styles_print["yellow"])
    selected_reward = questionary.text(
        "",
        style=styles_choice
    ).ask()
    return selected_reward


def starting_gear(selected_combat_proficiencies):
    title()
    if input("Would you like to have weapons?(y/n)").lower() == "y":
        weapons = []
        while True:
            title()
            print("Current weapon levels:\n")
            for name in selected_combat_proficiencies:
                print(f"{name}\t  :      {selected_combat_proficiencies[name]}")
            print("\nWeapons currently carried:\n")
            for weapon in weapons:
                print(weapon)
            print("\nSelect your starting weapons:\n")
            
            answer = questionary.select(
                "",
                choices=[
                    questionary.Choice(
                        title=[
                            ("class:white", a)
                        ],
                        value=a
                    ) for a in Weapons.names() if a != "Unarmed" and a not in weapons
                ],
                style=styles_choice
            ).ask()
            print(str(Weapons.by_name(answer)))
            if input("Would you like to add this weapon?(y/n)").lower() == "y":
                weapons.append(answer)
                if input("Would you like to add another weapon?(y/n)").lower() == "n":
                    break
            
    else:
        weapons = None

    title()
    if input("Would you like to have armour?(y/n)").lower() == "y":
        while True:
            title()
            print("Select your armour:\n")
            armour = questionary.select(
                "",
                choices=[
                    questionary.Choice(
                        title=[
                            ("class:white", a)
                        ],
                        value=a
                    ) for a in Armours.names()
                ],
                style=styles_choice
            ).ask()
            print(str(Armours.by_name(armour)))
            if input("Would you like to add this armour?(y/n)").lower() == "y":
                break
    else:
        armour = None

    title()
    if input("Would you like to have a shield?(y/n)").lower() == "y":
        while True:
            title()
            print("Select your starting shield:\n")
            shield = questionary.select(
                "",
                choices=[
                    questionary.Choice(
                        title=[
                            ("class:white", a)
                        ],
                        value=a
                    ) for a in Shields.names()
                ],
                style=styles_choice
            ).ask()
            print(str(Shields.by_name(shield)))
            if input("Would you like to add this shield?(y/n)").lower() == "y":
                break
    else:
        shield = None

    title()
    if input("Would you like to have headgear?(y/n)").lower() == "y":
        while True:
            title()
            print("Select your starting headgear:\n")
            headgear = questionary.select(
                "",
                choices=[
                    questionary.Choice(
                        title=[
                            ("class:white", a)
                        ],
                        value=a
                    ) for a in Headgears.names()
                ],
                style=styles_choice
            ).ask() 
            print(str(Headgears.by_name(headgear)))
            if input("Would you like to add this headgear?(y/n)").lower() == "y":
                break
    else:
        headgear = None

    return weapons, armour, shield, headgear


def main():
    title()
    selected_culture = select_culture()
    selected_attributes = select_attributes(selected_culture)
    selected_combat_proficiencies = select_combat_proficiencies(selected_culture)
    selected_distinctive_features = select_distinctive_features(selected_culture)
    selected_name = select_name()
    selected_age = select_age()
    selected_calling = select_calling()
    selected_favoured_skills = select_favoured_skills(selected_culture, selected_calling)
    selected_weapons, selected_armour, selected_shield, selected_headgear = starting_gear(selected_combat_proficiencies)
    selected_virtue = select_virtue()
    selected_reward = select_reward()
    active_character = Character(culture = selected_culture, 
                                  attribute_choice = selected_attributes, 
                                  weapon_skill_levels = selected_combat_proficiencies,
                                  distinctive_features = selected_distinctive_features,
                                  name = selected_name,
                                  age = selected_age,
                                  calling = selected_calling,
                                  favoured_skill_choices = selected_favoured_skills,
                                  starting_virtue = selected_virtue,
                                  starting_reward = selected_reward
                                  )
    for weapon in selected_weapons:
        active_character.add_weapon(Weapons.by_name(weapon))
    active_character.change_armour(Armours.by_name(selected_armour))
    active_character.change_shield(Shields.by_name(selected_shield))
    active_character.change_headgear(Headgears.by_name(selected_headgear))
    previous_experience(active_character)
    return active_character
    
    
if __name__ == "__main__":
    main()