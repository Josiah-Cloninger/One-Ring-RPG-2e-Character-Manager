import os

import questionary

from culture2 import Cultures2, Culture2, all_combat_proficiencies
from character2 import Character2


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


def culture():
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
            ) for culture_name in Cultures2.names()
        ],
        style=styles_choice
    ).ask()
    return Cultures2.by_name(answer)


def attributes(selected_culture: Culture2):
    title()
    culture_attributes = []
    enumerater = 0
    times_run = 0
    set_of_attributes = ""
    for a in selected_culture.attributes:
        for i in a:
            set_of_attributes += str(i)
            set_of_attributes += str(" : ")
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
    return answer


def select_combat_proficiencies(selected_culture: Culture2):
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

    return level_2_choice, level_1_choice


def distinctive_features(selected_background):
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


def main():
    title()
    selected_culture = culture()
    selected_attributes = attributes(selected_culture)
    selected_combat_proficiencies = select_combat_proficiencies(selected_culture)
    selected_distinctive_features = distinctive_features(selected_culture)
    
    # active_character = Character2(culture = selected_culture, 
    #                               attribute_choice = selected_attributes, 
    #                               weapon_skill_levels = selected_combat_proficiencies,
    #                               distinctive_features = selected_distinctive_features,
    #                               name = selected_name,
    #                               age = selected_age,
    #                               calling = selected_calling,
    #                               favoured_skill_choices = selected_favoured_skill_choices,
    #                               starting_virtue = selected_virtue,
    #                               starting_reward = selected_reward)
    


if __name__ == "__main__":
    main()