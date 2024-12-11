import os

import questionary
from questionary import print

from culture2 import Cultures2, Culture2, all_combat_proficiencies
from character2 import Character2
from calling2 import Calling2, Callings2
from gear2 import Weapons2, Armours2, Shields2, Headgears2


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
                ) for a in Weapons2.names()
            ],
            style=styles_choice
        ).ask()
        print(str(Weapons2.by_name(answer)))
        if input("Would you like to add this weapon?(y/n)").lower() == "y":
            weapons.append(answer)
            if input("Would you like to add another weapon?(y/n)").lower() == "n":
                break
        
else:
    weapons = None

