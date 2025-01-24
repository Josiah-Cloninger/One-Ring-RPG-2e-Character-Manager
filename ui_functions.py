from character import Character, save_character, load_character
import os, sys, random
import character_creation
import pickle


version = "1.0"


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
    "roll": "Rolls for the chosen skill", 
    "revert": "Reverts the character to the last manually saved state"
}


def clear_console(active_character: Character = None):
    os.system('cls' if os.name == 'nt' else 'clear')
    if active_character is not None:
        autosave(active_character)
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


def valid_attributes(active_character: Character):
    valid_attributes = []

    for attribute in dir(active_character):
        if not attribute.startswith("__") and not callable(getattr(active_character, attribute)):
            valid_attributes.append(attribute)

    for weapon in active_character.weapons:
        valid_attributes.append(f"{weapon.name.lower()}")

    valid_attributes.append("armour")
    valid_attributes.append("shield")
    valid_attributes.append("headgear")

    valid_attributes.append(active_character.name.lower())

    valid_attributes.sort()

    return valid_attributes


def simple_attributes(active_character: Character):
    """returns the list of attributes that are simple data types (int, float, str)"""
    attributes = []
    for attribute in dir(active_character):
        if not attribute.startswith("__") and not callable(getattr(active_character, attribute)):
            attributes.append(attribute)
    return attributes


def weapon_names(active_character: Character):
    weapon_names = []
    for weapon in active_character.weapons:
        weapon_names.append(weapon.name.lower())
    return weapon_names


def create_character():
    active_character = character_creation.main()
    if input("Would you like to save and continue with this character? (y/n)").lower() == "y":
        save_character(active_character, f"{active_character.name}.pickle")
        clear_console(active_character)
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
            clear_console(active_character)
            return
        elif character_name.lower() == "help":
            print("\nname of the character to load")
            print("menu")
            print("exit\n")
        else:
            try:
                active_character = load_character(f"{character_name}")
                break
            except FileNotFoundError:
                clear_console()
                print("No character with that name was found. Please enter a different name")
                character_name = input("> ").lower()
    clear_console(active_character)
    print(f"{active_character.name} successfully loaded!\n")
    return active_character


def exit():
    print("Goodbye!")
    sys.exit()


def save_current_character(active_character: Character):
    save_character(active_character, f"{active_character.name.lower()}.pickle")
    clear_console(active_character)
    print(f"{active_character.name} successfully saved!\n")


def show_attribute(active_character: Character, commands: list[str]):
    clear_console(active_character)

    attribute = commands[1]

    weapon_names = []
    for weapon in active_character.weapons:
        weapon_names.append(weapon.name.lower())
    
    if attribute is None:
        print("Enter the attribute you would like to show: ")
        attribute = input("> ").lower()
    
    if attribute == "help":
        print(f"Valid attributes include:\n {valid_attributes(active_character)}\n")
    elif attribute in weapon_names:
        print(f"{attribute}: {active_character.weapons[weapon_names.index(attribute)]}\n")
    elif attribute == active_character.name.lower():
        print(active_character)
    elif attribute in valid_attributes(active_character):
        print(f"{attribute}: {getattr(active_character, attribute)}\n")
    else:
        print("Invalid attribute\n")


def set_attribute(active_character: Character, commands: list[str]):
    clear_console(active_character)

    attribute = commands[1]
    if attribute is None:
        print("Enter the attribute you would like to change: ")
        attribute = input("> ").lower()
    
    if attribute == "help":
        print(f"Valid attributes include:\n {valid_attributes(active_character)}\n")

    while attribute not in valid_attributes(active_character):
        print(f"Invalid attribute. Valid attributes include:\n {valid_attributes(active_character)}\n")
        attribute = input("> ").lower()

    if attribute == "armour":
        armour_attribute = commands[2]
        if armour_attribute is None:
            clear_console(active_character)
            print(f"Your current armour is {active_character.armour.name}\n",
                    f"Protection: {active_character.armour.protection}\n",
                    f"Load: {active_character.armour.load}\n\n\n"
                    f"Enter the name of the attribute you would like to modify:")
            armour_attribute = input("> ").lower()
        while armour_attribute not in ["protection", "load", "name"]:
            print("Invalid attribute. Valid attributes include:\n protection\n load\n name\n")
            armour_attribute = input("> ").lower()

        value = commands[3]
        while True:
            if value is None:
                clear_console(active_character)
                print(f"Your current armour is {active_character.armour.name}\n",
                    f"Protection: {active_character.armour.protection}\n",
                    f"Load: {active_character.armour.load}\n\n\n", 
                    f"Enter the new value for {armour_attribute}: ")
                value = input("> ").lower()

            try:
                if type(getattr(active_character, attribute)) == int:
                    value = int(value)
                if type(getattr(active_character, attribute)) == float:
                    value = float(value)
            except ValueError:
                print("That is not a valid value for this attribute. Please enter a number value.")
            else:
                break
        
        match armour_attribute:
            case "name":
                active_character.armour.name = value
            case "protection":
                active_character.armour.protection = value
            case "load":
                active_character.armour.load = value
        

    elif attribute == "shield":
        shield_attribute = commands[2]
        if shield_attribute is None:
            clear_console(active_character)
            print(f"Your current shield is {active_character.shield.name}\n",
                    f"Parry_mod: {active_character.shield.parry_mod}\n",
                    f"Load: {active_character.shield.load}\n\n\n"
                    f"Enter the name of the attribute you would like to modify:")
            shield_attribute = input("> ").lower()
        while shield_attribute not in ["parry_mod", "load", "name"]:
            print("Invalid attribute. Valid attributes include:\n parry_mod\n load\n name\n")
            shield_attribute = input("> ").lower()

        value = commands[3]
        while True:
            if value is None:
                clear_console(active_character)
                print(f"Your current armour is {active_character.shield.name}\n",
                    f"Parry_mod: {active_character.shield.parry_mod}\n",
                    f"Load: {active_character.shield.load}\n\n\n", 
                    f"Enter the new value for {shield_attribute}: ")
                value = input("> ").lower()

            try:
                if type(getattr(active_character, attribute)) == int:
                    value = int(value)
                if type(getattr(active_character, attribute)) == float:
                    value = float(value)
            except ValueError:
                print("That is not a valid value for this attribute. Please enter a number value.")
            else:
                break
        
        match shield_attribute:
            case "name":
                active_character.shield.name = value
            case "parry_mod":
                active_character.shield.parry_mod = value
            case "load":
                active_character.shield.load = value
        
                
    elif attribute == "headgear":
        headgear_attribute = commands[2]
        if headgear_attribute is None:
            clear_console(active_character)
            print(f"Your current headgear is {active_character.headgear.name}\n",
                    f"Protection: {active_character.headgear.protection}\n",
                    f"Load: {active_character.headgear.load}\n\n\n"
                    f"Enter the name of the attribute you would like to modify:")
            headgear_attribute = input("> ").lower()
        while headgear_attribute not in ["protection", "load", "name"]:
            print("Invalid attribute. Valid attributes include:\n protection\n load\n name\n")
            headgear_attribute = input("> ").lower()

        value = commands[3]
        while True:
            if value is None:
                clear_console(active_character)
                print(f"Your current armour is {active_character.headgear.name}\n",
                    f"Protection: {active_character.headgear.protection}\n",
                    f"Load: {active_character.headgear.load}\n\n\n", 
                    f"Enter the new value for {headgear_attribute}: ")
                value = input("> ").lower()

            try:
                if type(getattr(active_character, attribute)) == int:
                    value = int(value)
                if type(getattr(active_character, attribute)) == float:
                    value = float(value)
            except ValueError:
                print("That is not a valid value for this attribute. Please enter a number value.")
            else:
                break
        
        match headgear_attribute:
            case "name":
                active_character.headgear.name = value
            case "protection":
                active_character.headgear.protection = value
            case "load":
                active_character.headgear.load = value


    elif attribute in weapon_names(active_character):
        weapon_attribute = commands[2]
        weapon_index = weapon_names(active_character).index(attribute)
        if weapon_attribute is None:
            clear_console(active_character)
            print(f"Your {attribute}'s current stats are:\n",
                  f"Name: {active_character.weapons[weapon_index].name}\n",
                  f"Damage: {active_character.weapons[weapon_index].damage}\n",
                  f"Injury: {active_character.weapons[weapon_index].injury}\n",
                  f"Load: {active_character.weapons[weapon_index].load}\n",
                  f"Notes: {active_character.weapons[weapon_index].notes}\n\n\n",
                  f"Enter the name of the attribute you would like to modify:")
            weapon_attribute = input("> ").lower()
        while weapon_attribute not in ["name", "damage", "injury", "load", "notes"]:
            print("Invalid attribute. Valid attributes include:\n name\n damage\n injury\n load\n notes\n")
            weapon_attribute = input("> ").lower()

        value = commands[3]
        while True:
            if value is None:
                clear_console(active_character)
                print(f"Your {attribute}'s current stats are:\n",
                      f"Name: {active_character.weapons[weapon_index].name}\n",
                      f"Damage: {active_character.weapons[weapon_index].damage}\n",
                      f"Injury: {active_character.weapons[weapon_index].injury}\n",
                      f"Load: {active_character.weapons[weapon_index].load}\n",
                      f"Notes: {active_character.weapons[weapon_index].notes}\n\n\n", 
                      f"Enter the new value for {weapon_attribute}: ")
                value = input("> ").lower()

            try:
                if type(getattr(active_character.weapons[weapon_index], weapon_attribute)) == int:
                    value = int(value)
                if type(getattr(active_character.weapons[weapon_index], weapon_attribute)) == float:
                    value = float(value)
            except ValueError:
                print("That is not a valid value for this attribute. Please enter a number value.")
            else:
                break
        
        match weapon_attribute:
            case "name":
                active_character.weapons[weapon_index].name = value
            case "damage":
                active_character.weapons[weapon_index].damage = value
            case "injury":
                active_character.weapons[weapon_index].injury = value
            case "load":
                active_character.weapons[weapon_index].load = value
            case "notes":
                active_character.weapons[weapon_index].notes = value

        
    elif attribute in simple_attributes(active_character):
        value = commands[2]
        while True:
            if value is None:
                print(f"{attribute} is currently set to {getattr(active_character, attribute)}. \n\n\nEnter the new value for {attribute}: ")
                value = input("> ").lower()

            try:
                if type(getattr(active_character, attribute)) == int:
                    value = int(value)
                if type(getattr(active_character, attribute)) == float:
                    value = float(value)
            except ValueError:
                print("That is not a valid value for this attribute. Please enter a number value.")
            else:
                break
        setattr(active_character, attribute, value)

    clear_console(active_character)

    print(f"Successfully set {attribute} to {value}\n")

        
def roll_skill(active_character: Character, attribute: str):
    clear_console(active_character)
    if attribute is None:
        print("Enter the attribute you would like to roll:")
        attribute = input("> ").lower()
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
    clear_console(active_character)
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


def autosave(active_character: Character):
    with open(f"{active_character.name}_autosave.pickle", "wb") as file:
        pickle.dump(active_character, file)
