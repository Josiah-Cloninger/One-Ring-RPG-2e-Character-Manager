from ui_functions import (clear_console, start_help, create_character, 
                          select_character_to_load, save_current_character, 
                          show_attribute, set_attribute, roll_attribute, help, update_character)
from character import load_character


active_character = None

clear_console()

# Either load an existing character, or create a new one
while active_character is None:
        print("Please start by either loading an exhisting character with 'load' or creating a new character with 'create'")
        string_input = input("> ").lower()
        input_list = string_input.split()
        match input_list[0]:
            case "help":
                start_help()
            case "exit":
                exit()
            case "create":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load(input_list[1])
            case _:
                clear_console()
                print("Invalid command\n\n")
    
# The main menu for the character manager. Should only be here with an "active character"
while True:
    print("Enter a command:")
    string_input = input("> ").lower()
    input_list = string_input.split()
    match input_list[0]:
        case "help":
            help()
        case "exit":
            exit()
        case "create":
            active_character = create_character()
        case "load":
            active_character = select_character_to_load(input_list)
        case "save":
            save_current_character(active_character)
        case "show":
            show_attribute(active_character, input_list)
        case "set":
            set_attribute(active_character, input_list)
        case "roll":
            roll_attribute(active_character, input_list)
        case "revert":
            clear_console()
            active_character = load_character(active_character.name)
            print("Character reverted to the last manually saved state\n")
        case "update":
            update_character(active_character)
        case _:
            print("Invalid command\n")
