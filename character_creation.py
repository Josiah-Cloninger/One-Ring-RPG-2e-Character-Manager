"""Module for character creation, run as main."""

import os
import questionary

from culture import Cultures, Culture
from character import Character
from calling import Calling, Callings
from gear import Weapons, Armours, Shields, Headgears
from boons import Virtue, Reward


STYLES_PRINT = {
    "culture": "#0001e0",
    "yellow": "#deea0b",
    "specialty": "#4fdb5a",
    "background": "#f78400",
    "white": "#ffffff"
}

STYLES_CHOICE = questionary.Style([
    ('yellow', '#deea0b'),
    ('culture', '#0001e0'),
    ('specialty', '#4fdb5a'),
    ('background', '#f78400'),
    ('white', '#ffffff')
])

VERSION = "2.02"


def clear_console():
    """Clears the console and prints the title. If a character object is passed, it will autosave that character."""
    os.system('cls' if os.name == 'nt' else 'clear')
    questionary.print(f"One Ring RPG Character Manager\n"
          f"Version: {VERSION}\n"
          f"Enter 'help' at any time for a list of commands or 'exit' to quit\n\n")

def select_culture():
    """Walk the user through selecting a culture."""
    clear_console()
    questionary.questionary.print("Select Culture:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE
    ).ask()
    return Cultures.by_name(answer)

def select_attributes(selected_culture: Culture):
    """Walk the user through selecting attributes."""
    clear_console()
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
    questionary.questionary.print("Select Attributes:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE
    ).ask()

    # generating the dictionary required by the __init__ function for the character class
    attributes_list = answer.split(", ")

    attributes_dict = {}

    for attribute in attributes_list:
        attribute_name, attribute_value = attribute.split(": ")
        attributes_dict[attribute_name] = int(attribute_value)

    return attributes_dict

def select_combat_proficiencies(selected_culture: Culture):
    """Walk the user through selecting combat proficiencies."""
    clear_console()

    # selecting one of the combat proficiencies indicated by your culture to start at level 2
    questionary.questionary.print("Select one of the following Combat Proficiencies to start at level 2:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE
    ).ask()

    # selecting one of any combat proficiencies to start at level 1
    questionary.questionary.print("Select one of the following Combat Proficiencies to start at level 1:\n", style=STYLES_PRINT["yellow"])
    level_1_choice = questionary.select(
        "",
        choices=[
            questionary.Choice(
                title=[
                    ("class:white", proficiency)

                ],
                value=proficiency
            )for proficiency in [x for x in ["axes", "bows", "spears", "swords"] if x != level_2_choice]
        ],
        style=STYLES_CHOICE
    ).ask()

    # generating the dictionary required by the __init__ function for the character class
    combat_proficiencies = {"axes": 0, "bows": 0, "spears": 0, "swords": 0}

    combat_proficiencies.update({level_2_choice: 2})
    combat_proficiencies.update({level_1_choice: 1})

    return combat_proficiencies

def select_distinctive_features(selected_background):
    """Walk the user through selecting distinctive features."""
    clear_console()
    questionary.questionary.print("Select Distinctive Features:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE,
        validate=lambda answer: "Please select two distinctive features." if len(answer) != 2 else True
    ).ask()
    return selected_distinctive_features

def select_name():
    """Walk the user through selecting a name."""
    clear_console()
    questionary.questionary.print("Enter Name:\n", style=STYLES_PRINT["yellow"])
    selected_name = questionary.text(
        "",
        style=STYLES_CHOICE
    ).ask()
    return selected_name

def select_age():
    """Walk the user through selecting an age."""
    clear_console()
    questionary.questionary.print("Enter Age:\n", style=STYLES_PRINT["yellow"])
    selected_age = questionary.text(
        "",
        style=STYLES_CHOICE
    ).ask()
    return selected_age

def select_calling():
    """Walk the user through selecting a calling."""
    clear_console()
    questionary.questionary.print("Select Calling:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE
    ).ask()
    return Callings.by_name(answer)

def select_favoured_skills(selected_culture: Culture,selected_calling: Calling):
    """Walk the user through selecting favoured skills."""
    favoured_skills = []
    choice_1 = []
    choice_2 = []
    clear_console()

    # selecting favoured skill from culture
    questionary.questionary.print("Select one favoured skill from you culture:\n", style=STYLES_PRINT["yellow"])
    choice_1.append(questionary.select(
            "",
            choices=[
                questionary.Choice(
                    title=[
                        ("class:white", skill_name)
                    ],
                    value=skill_name
                ) for skill_name in selected_culture.favoured_skills
            ],
            style=STYLES_CHOICE
        ).ask()
    )

    # selecting two favoured skills from calling
    questionary.questionary.print("Select two favoured skills from your calling:\n", style=STYLES_PRINT["yellow"])
    choice_2.append(questionary.checkbox(
            "",
            choices=[
                questionary.Choice(
                    title=[
                        ("class:white", a)
                    ],
                    value=a
                ) for a in selected_calling.favoured_skills if a not in choice_1
            ],
            style=STYLES_CHOICE,
            validate=lambda answer: "Please select two favoured skills." if len(answer) != 2 else True
        ).ask()
    )
    for skill in choice_1 + choice_2:
        favoured_skills.append(skill)
    return favoured_skills

def select_skill_upgrade(character: Character):
    """Walk the user through selecting a skill to upgrade."""
    clear_console()
    questionary.questionary.print("Upgrade Common Skill:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE
    ).ask()
    return answer

def upgrade_skill(character: Character, skill: str, previous_experience_points: int):
    """Upgrade a skill."""
    if previous_experience_points >= character.skill_levels[skill] + 1:
        character.skill_levels[skill] += 1
        previous_experience_points -= character.skill_levels[skill]
        return previous_experience_points
    else:
        questionary.print("You do not have enough experience to upgrade this skill.")
        return previous_experience_points

def select_weapon_skill_upgrade(character: Character):
    """Walk the user through selecting a combat proficiency to upgrade."""
    clear_console()
    questionary.questionary.print("Upgrade Weapon Skill:\n", style=STYLES_PRINT["yellow"])
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
        style=STYLES_CHOICE
    ).ask()
    return answer

def upgrade_weapon_skill(character: Character, skill: str, previous_experience_points: int):
    """Upgrade a combat proficiency."""
    if previous_experience_points >= character.combat_proficiencies[skill] * 2 + 2:
        character.combat_proficiencies[skill] += 1
        previous_experience_points -= character.combat_proficiencies[skill] * 2
        return previous_experience_points
    else:
        questionary.print("You do not have enough experience to upgrade this skill.")
        return previous_experience_points

def previous_experience(character: Character):
    """Walk the user through upgrading skills and combat proficiencies."""
    continue_loop = True
    previous_experience_points = 10
    while previous_experience_points > 0 and continue_loop:
        clear_console()
        questionary.print("Skill Levels:\n", style=STYLES_PRINT["yellow"])
        for skill, level in character.skill_levels.items():
            questionary.print(f"{skill}: {level}")
        questionary.print("Combat Proficiency Levels:\n", style=STYLES_PRINT["yellow"])
        for skill, level in character.combat_proficiencies.items():
            questionary.print(f"{skill}: {level}")
        questionary.print("\nPoints Remaining:\n", style=STYLES_PRINT["yellow"])
        questionary.print(str(previous_experience_points))
        questionary.print("\n")
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
            style=STYLES_CHOICE,
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
    """Walk the user through selecting a virtue."""
    clear_console()
    selected_virtue = Virtue()

    questionary.questionary.print("Enter the name of the virtue you would like to add:\n", style=STYLES_PRINT["yellow"])
    selected_virtue.name = questionary.text(
        "",
        style=STYLES_CHOICE
    ).ask()

    questionary.questionary.print("Enter the effect of the virtue you would like to add:\n", style=STYLES_PRINT["yellow"])
    selected_virtue.effect = questionary.text(
        "",
        style=STYLES_CHOICE
    ).ask()

    return selected_virtue

def select_reward():
    """Walk the user through selecting a reward."""
    clear_console()
    selected_reward = Reward()

    questionary.questionary.print("Enter the name of the reward you would like to add:\n", style=STYLES_PRINT["yellow"])
    selected_reward.name = questionary.text(
        "",
        style=STYLES_CHOICE
    ).ask()

    questionary.questionary.print("Enter the effect of the reward you would like to add:\n", style=STYLES_PRINT["yellow"])
    selected_reward.effect = questionary.text(
        "",
        style=STYLES_CHOICE
    ).ask()

    return selected_reward

def starting_gear(selected_combat_proficiencies):
    """Walk the user through selecting starting gear."""
    clear_console()
    if input("Would you like to have weapons?(y/n)").lower() == "y":
        weapons = []
        while True:
            clear_console()
            questionary.print("Current weapon levels:\n")
            for name in selected_combat_proficiencies:
                questionary.print(f"{name}\t  :      {selected_combat_proficiencies[name]}")
            questionary.print("\nWeapons currently carried:\n")
            for weapon in weapons:
                questionary.print(weapon)
            questionary.print("\nSelect your starting weapons:\n")

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
                style=STYLES_CHOICE
            ).ask()
            questionary.print(str(Weapons.by_name(answer)))
            if input("Would you like to add this weapon?(y/n)").lower() == "y":
                weapons.append(answer)
                if input("Would you like to add another weapon?(y/n)").lower() == "n":
                    break

    else:
        weapons = None

    clear_console()
    if input("Would you like to have armour?(y/n)").lower() == "y":
        while True:
            clear_console()
            questionary.print("Select your armour:\n")
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
                style=STYLES_CHOICE
            ).ask()
            questionary.print(str(Armours.by_name(armour)))
            if input("Would you like to add this armour?(y/n)").lower() == "y":
                break
    else:
        armour = None

    clear_console()
    if input("Would you like to have a shield?(y/n)").lower() == "y":
        while True:
            clear_console()
            questionary.print("Select your starting shield:\n")
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
                style=STYLES_CHOICE
            ).ask()
            questionary.print(str(Shields.by_name(shield)))
            if input("Would you like to add this shield?(y/n)").lower() == "y":
                break
    else:
        shield = None

    clear_console()
    if input("Would you like to have headgear?(y/n)").lower() == "y":
        while True:
            clear_console()
            questionary.print("Select your starting headgear:\n")
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
                style=STYLES_CHOICE
            ).ask()
            questionary.print(str(Headgears.by_name(headgear)))
            if input("Would you like to add this headgear?(y/n)").lower() == "y":
                break
    else:
        headgear = None

    return weapons, armour, shield, headgear

def main():
    """Walk the user through the character creation process."""
    clear_console()
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
                                  favoured_skills = selected_favoured_skills,
                                  starting_virtue = selected_virtue,
                                  starting_reward = selected_reward
                                  )
    if selected_weapons is not None:
        for weapon in selected_weapons:
            active_character.weapons.append(Weapons.by_name(weapon))
    active_character.armour = Armours.by_name(selected_armour)
    active_character.shield = Shields.by_name(selected_shield)
    active_character.headgear = Headgears.by_name(selected_headgear)
    previous_experience(active_character)
    return active_character


if __name__ == "__main__":
    main()
