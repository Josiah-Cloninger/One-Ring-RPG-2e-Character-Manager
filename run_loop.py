from ui_functions import (clear_console, start_help, create_character, 
                          select_character_to_load, save_current_character, 
                          show_attribute, set_attribute, roll_skill, help)
from character import load_character


active_character = None


clear_console(active_character)
while True:
    if active_character is None:
        print("Please start by either loading an exhisting character with 'load' or creating a new character with 'create'")
        user_commands = input("> ").lower()
        user_commands = user_commands.split()
        user_commands.extend([None]*(10 - len(user_commands)))
        match user_commands[0]:
            case "help":
                start_help()
            case "exit":
                exit()
            case "create":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load(user_commands[1])
            case _:
                print("Invalid command\n")
    else:
        print("\nEnter a command:")
        user_commands = input("> ").lower()
        user_commands = user_commands.split()
        user_commands.extend([None]*(10 - len(user_commands)))
        match user_commands[0]:
            case "help":
                help()
            case "exit":
                exit()
            case "create":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load(user_commands[1])
            case "save":
                save_current_character(active_character)
            case "show":
                show_attribute(active_character, user_commands)
            case "set":
                set_attribute(active_character, user_commands)
            case "roll":
                roll_skill(active_character, user_commands[1])
            case "revert":
                active_character = load_character(f"{active_character.name.lower()}_hardsave.pickle")
            case _:
                print("Invalid command\n")
