import os, sys, types


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

commands = {
    "help": "Prints a list of commands",
    "exit": "Exits the program",
    "create character": "Creates a new character",
    "load": "Loads a character",
    "save": "Saves the current character"
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()


def title():
    print("One Ring RPG Character Manager\n"
          "Enter \'help\' at any time for a list of commands or \'exit\' to quit\n")


def start_help():
    print("\n")
    for command, description in start_commands.items():
        print(f"{command}: {description}")
    print("\n")


def help():
    print("\n")
    for command, description in commands.items():
        print(f"{command}: {description}")
    print("\n")


def attr_help():
    print("\n")
    print("availabe attributes include:\n")
    for attr in dir(active_character):
        if not attr.startswith("__") and not callable(getattr(active_character, attr)):
            print(f"{attr}")
    print("\n")


def create_character():
    active_character = character_creation.main()
    if input("Would you like to save and continue with this character? (y/n)").lower() == "y":
        save_character(active_character, f"{active_character.name}.pickle")
        clear_console()
        print(f"{active_character.name} successfully created and saved!")   
        return active_character         
                

def select_character_to_load():
    print("Enter the name of the character to load: ")
    filename = input("> ").lower()

    while True:
        try:
            active_character = load_character(f"{filename}.pickle")
            break
        except FileNotFoundError:
            print("No character with that name was found. Please enter a different name")
            filename = input("> ").lower()

    clear_console()
    print(f"{active_character.name} successfully loaded!\n")
    return active_character


def exit():
    print("Goodbye!")
    sys.exit()


def save_current_character(active_character: Character2):
    save_character(active_character, f"{active_character.name.lower()}.pickle")
    clear_console()
    print(f"{active_character.name} successfully saved!\n")


def show_attributes(active_character: Character2):
    clear_console()
    while True:
        print("Enter the attribute you would like to see:\n")
        command = input("> ")
        match command:
            case "exit":
                break
            case "help":
                attr_help()
            case _:
                try:
                    clear_console()
                    print(f"{command}: {getattr(active_character, command)}\n")
                except AttributeError:
                    clear_console()
                    print("Attribute not fond\n")


clear_console()
while True:
    if active_character is None:
        print("Please start by either loading an exhisting character with \'load\' or creating a new character with \'create character\'")
        command = input("> ")
        match command:
            case "help":
                start_help()
            case "exit":
                exit()
            case "create character":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load()
            case _:
                print("Invalid command\n")
    else:
        print("Enter a command:")
        command = input("> ")
        match command:
            case "help":
                help()
            case "exit":
                exit()
            case "create character":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load()
            case "save":
                save_current_character(active_character)
            case "show":
                show_attributes(active_character)
            case _:
                print("Invalid command\n")
