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


def clear_console(active_character):
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    clear_console(active_character)
    questionary.print("The One Rings RPG Character Sheet\n", style=styles_print["yellow"])

title()
if input("Would you like to have weapons?(y/n)").lower() == "y":
    weapons = []
    while True:
        title()
        print("Select your starting weapons:\n")
        answer = questionary.select(
            "",
            choices=[
                questionary.Choice(
                    title=[
                        ("class:white", a)
                    ],
                    value=a
                ) for a in Weapons.names()
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

