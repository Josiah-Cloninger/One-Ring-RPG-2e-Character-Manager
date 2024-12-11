import os
import sys

import character_creation


from character2 import Character2, load_character, save_character

active_character = None
start_commands = {
    "help": "Prints a list of commands",
    "exit": "Exits the program",
    "create character": "Creates a new character",
    "load": "Loads a character",
    "save": "Saves a character",
    "show": "Shows attributes of a character"
}



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    clear_console()
    print("One Ring RPG Character Manager\n\n")


def help():
    title()
    for command, description in start_commands.items():
        print(f"{command}: {description}")
    input("Press enter to continue")


def create_character():
    title()
    active_character = character_creation.main()
    if input("Would you like to save and continue with this character? (y/n)").lower() == "y":
        save_character(active_character, f"{active_character.name}.pickle")
        print("Character saved!")   
        input("Press enter to continue")
        return active_character         
                

def select_character_to_load():
    title()
    print("Enter the name of the character to load: ")
    filename = input("> ")
    active_character = load_character(f"{filename}.pickle")
    return active_character


def exit():
    print("Goodbye!")
    sys.exit()


def save_current_character(active_character: Character2):
    title()
    save_character(active_character, f"{active_character.name}.pickle")
    print("Character saved!")
    input("Press enter to continue")

def show_attributes(active_character: Character2):
    while True:
        title()
        print("What would you like to see?\n")
        command = input("> ")
        if command == "exit":
            break
        try:
            print(getattr(active_character, command))
            print("Press enter to continue, or type 'exit' to return to the main menu")
            command = input("> ")
            if command == "exit":
                break
        except AttributeError:
            print("Invalid command.")
            print("Press enter to continue, or type 'exit' to return to the main menu")
            command = input("> ")
            if command == "exit":
                break


clear_console()
input("Welcome to the One Ring RPG Character Manager!\nEnter 'help' for a list of commands\nPress enter to continue")

while True:
    title()
    command = input("> ")
    if active_character is None:
        if command == "help":
            help()
        elif command == "exit":
            exit()
        elif command == "create character":
            active_character = create_character()
        elif command == "load":
            active_character = select_character_to_load()
        else:
            print("Invalid command.")
            input("Press enter to continue")
    else:
        if command == "help":
            help()
        elif command == "exit":
            exit()
        elif command == "create character":
            active_character = create_character()
        elif command == "load":
            active_character = select_character_to_load()
        elif command == "save":
            save_current_character(active_character)
        elif command == "show":
            show_attributes(active_character)
        else:
            print("Invalid command.")
            input("Press enter to continue")
