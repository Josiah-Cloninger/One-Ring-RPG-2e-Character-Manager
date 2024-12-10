import os

import questionary

from culture2 import Cultures2, Culture2


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
    selected_distinctive_features = distinctive_features(selected_culture)
    


if __name__ == "__main__":
    main()