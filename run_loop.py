import os, sys, types, random


import character_creation


from character import Character, load_character, save_character
from dice_roller import roll


active_character = None


start_commands = {
    "help": "Prints a list of commands",
    "exit": "Exits the program",
    "create": "Creates a new character",
    "load": "Loads a character",
    "save": "Saves a character",
    "show": "Shows attributes of a character"
}


commands = {
    "help": "Prints a list of commands",
    "exit": "Exits the program",
    "create character": "Creates a new character",
    "load": "Loads a character",
    "save": "Saves the current character",
    "set": "Sets character's attributes",
    "show": "Shows attributes of a character",
    "roll": "Rolls for the chosen skill"
}


version = "0.1"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()


def title():
    print("One Ring RPG Character Manager\nVersion : " + version + "\n"
        "Enter 'help' at any time for a list of commands or 'exit' to quit\n\n")


def start_help():
    print("\n")
    for command, description in start_commands.items():
        print(f"{command}: {description}")
    print("\n")


def help():
    clear_console()
    print("Valid commands include:\n")
    for command, description in commands.items():
        print(f"{command}: {description}")
    print()


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
                

def select_character_to_load(character_name: str):
    while True:
        if character_name is None:
            print("Enter the name of the character to load: ")
            character_name = input("> ").lower()
        if character_name.lower() == "exit":
            exit()
        elif character_name.lower() == "menu":
            clear_console()
            return
        elif character_name.lower() == "help":
            print("\nname of the character to load")
            print("menu")
            print("exit\n")
        else:
            try:
                active_character = load_character(f"{character_name}.pickle")
                break
            except FileNotFoundError:
                print("No character with that name was found. Please enter a different name")
                character_name = input("> ").lower()
        character_name = None
    clear_console()
    print(f"{active_character.name} successfully loaded!\n")
    return active_character


def exit():
    print("Goodbye!")
    sys.exit()


def save_current_character(active_character: Character):
    save_character(active_character, f"{active_character.name.lower()}.pickle")
    clear_console()
    print(f"{active_character.name} successfully saved!\n")


def show_attributes(active_character: Character, attribute: str):
    clear_console()
    if attribute is None:
        print("Enter the attribute you would like to see:")
        attribute = input("> ")
    if attribute == "help":
        clear_console()
        attr_help()
    elif attribute == str(active_character.name.lower()):
        clear_console()
        print(active_character)
    else:
        clear_console()
        try:
            print(f"{attribute}: {getattr(active_character, attribute)}\n")
        except AttributeError:
            print("Attribute not found\n")


def set_attributes(active_character: Character, attribute: str, value):
    clear_console()
    if attribute is None:
        print("Enter the attribute you would like to set:")  
        attribute = input("> ")
    match attribute:
        case "help":
            attr_help()
        case _:
            try:
                clear_console()
                print(f"{attribute}: {getattr(active_character, attribute)}\n")
                if value is None:
                    print(f"Enter what you would like to change {attribute} to:")
                    value = input("> ")
                attr_type=type(getattr(active_character, attribute))
                match attr_type:
                    case int:
                        value = int(value)
                setattr(active_character, attribute, value)
                clear_console()
                print(f"{attribute} successfully changed to {getattr(active_character, attribute)}\n")
            except AttributeError:
                clear_console()
                print("Attribute not fond")


def modify_attributes(active_character: Character, attribute: str, value):
    clear_console()
    if attribute is None:
        print("Enter the attribute you would like to modify:")  
        attribute = input("> ")
    match attribute:
        case "help":
            attr_help()
        case "virtue":
            if value is None:
                print("Enter the name of the virtue you would like to add:")
                value = input("> ")
            active_character.add_virtue(value)
            clear_console()
            print(f"{value} successfully added to virtues\n")
        case "reward":
            if value is None:
                print("Enter the name of the reward you would like to add:")
                value = input("> ")
            active_character.add_reward(value)
            clear_console()
            print(f"{value} successfully added to rewards\n")
        case _:
            try:
                print(f"{attribute}: {getattr(active_character, attribute)}\n")
                if value is None:
                    print(f"Enter how much you would like to change {attribute} by:")
                    value = input("> ")
                attr_type=type(getattr(active_character, attribute))
                match attr_type:
                    case int:
                        value = int(value)
                setattr(active_character, attribute, getattr(active_character, attribute) +value)
                clear_console()
                print(f"{attribute} successfully changed to {getattr(active_character, attribute)}\n")
            except AttributeError:
                clear_console()
                print("Attribute not fond")


def roll_skill(active_character: Character, attribute: str):
    clear_console()
    if attribute is None:
        print("Enter the attribute you would like to roll:")
        attribute = input("> ")
    match attribute:
        case "help":
            for i in rollable_items(active_character):
                print(i)
            print("\n")
        case _:
            rollable_list = rollable_items(active_character)
            advantage, disadvantage = has_advantage_or_disadvange()
            if attribute == "armour":
                total, feat_die, quality_of_success = roll(int(active_character.armour.protection), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "bows_skill":
                total, feat_die, quality_of_success = roll(int(active_character.combat_proficiencies["bows"]), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "swords_skill":
                total, feat_die, quality_of_success = roll(int(active_character.combat_proficiencies["swords"]), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "axes_skill":
                total, feat_die, quality_of_success = roll(int(active_character.combat_proficiencies["axes"]), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "spears_skill":
                total, feat_die, quality_of_success = roll(int(active_character.combat_proficiencies["spears"]), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute in rollable_list:
                total, feat_die, quality_of_success = roll(int(active_character.skill_levels[attribute]), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "wit_score":
                total, feat_die, quality_of_success = roll(int(active_character.wits_score), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "strength_score":
                total, feat_die, quality_of_success = roll(int(active_character.strength_score), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            elif attribute == "heart_score":
                total, feat_die, quality_of_success = roll(int(active_character.heart_score), advantage, disadvantage)
                print_roll(total, feat_die, quality_of_success)
            else:
                print("Attribute not found\n")


def has_advantage_or_disadvange():
    user_input = input("Do you have advantage (y/n)\n> ").lower()
    if user_input == "y":
        advantage = True
    else:
        advantage = False
    user_input = input("Do you have disadvantage (y/n)\n> ").lower()
    if user_input == "y":
        disadvantage = True
    else:
        disadvantage = False
    return advantage, disadvantage


def print_roll(total, feat_die, quality_of_success):
    clear_console()
    print(f"You got {total},")
    print(f"the Feat Die was {feat_die},")
    if quality_of_success == 0:
        print("and you got a ordinary success!\n")
    elif quality_of_success == 1:
        print("and you got a great success!\n")
    elif quality_of_success == 2:
        print("and you got a extrodanary success!\n")


def roll(dice_to_roll, advantage, disadvantage):
    while True:
        total = 0
        quality_of_success = 0
        feat_die = random.randint(1,12)
        if advantage:
            if not disadvantage:
                new_feat_roll = random.randint(1,12)
                if new_feat_roll > feat_die:
                    feat_die = new_feat_roll
        elif disadvantage:
            new_feat_roll = random.randint(1,12)
            if new_feat_roll < feat_die:
                feat_die = new_feat_roll
        total += feat_die
        while dice_to_roll > 0:
            die = random.randint(1,6)
            if die == 6:
                quality_of_success += 1
            total += die
            dice_to_roll -= 1
        if quality_of_success > 2:
            quality_of_success = 2
        return total, feat_die, quality_of_success
    

def rollable_items(active_character: Character):
    clear_console()
    rollable_list = []
    for skill in active_character.skill_levels:
        rollable_list.append(skill)
    rollable_list.append("axes_skill")
    rollable_list.append("bows_skill")
    rollable_list.append("swords_skill")
    rollable_list.append("spears_skill")
    if active_character.armour is not None:
        rollable_list.append("armour")
    rollable_list.append("wit_score")
    rollable_list.append("strength_score")
    rollable_list.append("heart_score")
    return rollable_list


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
                show_attributes(active_character, user_command[1])
            case "set":
                set_attributes(active_character, user_command[1], user_command[2])
            case "modify":
                modify_attributes(active_character, user_command[1], user_command[2])
            case "roll":
                roll_skill(active_character, user_command[1])
            case _:
                print("Invalid command\n")
