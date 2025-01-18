from ui_functions import (clear_console, start_help, create_character, 
                          select_character_to_load, save_current_character, 
                          show_attribute, roll_skill)


active_character = None


clear_console()
while True:
    if active_character is None:
        print("Please start by either loading an exhisting character with 'load' or creating a new character with 'create'")
        user_command = input("> ").lower()
        user_command = user_command.split()
        user_command.extend([None]*(10 - len(user_command)))
        match user_command[0]:
            case "help":
                start_help()
            case "exit":
                exit()
            case "create":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load(user_command[1])
            case _:
                print("Invalid command\n")
    else:
        print("\nEnter a command:")
        user_command = input("> ").lower()
        user_command = user_command.split()
        user_command.extend([None]*(10 - len(user_command)))
        match user_command[0]:
            case "help":
                help()
            case "exit":
                exit()
            case "create":
                active_character = create_character()
            case "load":
                active_character = select_character_to_load(user_command[1])
            case "save":
                save_current_character(active_character)
            case "show":
                show_attribute(active_character, user_command[1])
            case "roll":
                roll_skill(active_character, user_command[1])
            case _:
                print("Invalid command\n")
