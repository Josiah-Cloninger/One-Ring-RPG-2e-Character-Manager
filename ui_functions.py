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
}

commands = {
    "help": "Prints a list of commands.",
    "exit": "Exits the program.",
    "create character": "Creates a new character.",
    "load": "Loads a character.",
    "save": "Saves the current character.",
    "set": "Sets character's attributes.",
    "show": "Shows attributes of a character.",
    "roll": "Rolls for the chosen skill.", 
    "revert": "Reverts the character to the last manually saved state."
}

viewable_attributes = {
    "Name": "Your character's name",

    "Culture": "Your character's heroic culture",
    "Blessing": "Your character's cultural blessing",
    "Calling": "Your character's calling",

    "Age": "Your character's age",
    "Standard of Living": "Your character's standard of living",
    "Treasure": "Your character's treasure rating",
    "Patron": "Your character's patron",
    "Shadow Path": "Your character's shadow path",

    "Distinctive Features": "Your character's distinctive features",
    "Flaws": "Your character's flaws",

    # Attributes and Derived Stats
    "Strength": "Your character's strength rating",
    "Strength TN": "The TN for your character's Strength Skills",
    "Max Endurance": "Your character's maximum endurance",

    "Heart": "Your character's heart rating",
    "Heart TN": "The TN for your character's Heart Skills",
    "Max Hope": "Your character's maximum hope",

    "Wits": "Your character's wits rating",
    "Wits TN": "The TN for your character's Wits Skills",
    "Parry": "Your character's parry rating",

    # Skills
    "Awe": "Your character's awe skill level",
    "Athletics": "Your character's athletics skill level",
    "Awareness": "Your character's awareness skill level",
    "Hunting": "Your character's hunting skill level",
    "Song": "Your character's song skill level",
    "Craft": "Your character's craft skill level",

    "Enhearten": "Your character's enhearten skill level",
    "Travel": "Your character's travel skill level",
    "Insight": "Your character's insight skill level",
    "Healing": "Your character's healing skill level",
    "Courtesy": "Your character's courtesy skill level",
    "Battle": "Your character's battle skill level",

    "Persuade": "Your character's persuade skill level",
    "Stealth": "Your character's stealth skill level",
    "Scan": "Your character's scan skill level",
    "Explore": "Your character's explore skill level",
    "Riddle": "Your character's riddle skill level",
    "Lore": "Your character's lore skill level",

    # Combat Proficencies
    "Axes": "Your character's axes proficincey level",
    "Bows": "Your character's bows proficincey level",
    "Spears": "Your character's spears proficincey level",
    "Swords": "Your character's swords proficincey level",

    # Valour/Wisdom
    "Valour": "Your character's valour rating",
    "Rewards": "A list of your character's rewards",
    "Wisdom": "Your character's wisdom rating",
    "Virtues": "A list of your character's virtues",

    # Gear
    "Weapons": "A list of your character's weapons",
    "Armour": "Your character's armour",
    "Shield": "Your character's shield",
    "Headgear": "Your character's headgear",
    "Traveling Gear": "Your character's travelling gear",

    # Other
    "Adventure Points": "Your character's adventure points",
    "Skill Points": "Your character's skill points",
    "Fellowship Score": "Your character's fellowship score",

    # Endurance/Hope
    "Current Endurance": "Your character's current endurance",
    "Load": "The combined load of all your character's war gear and fatigue",
    "Fatigue": "Your character's fatigue level",
    "Current Hope": "Your character's current hope",
    "Shadow": "Your character's shadow points and shadow scars combined",
    "Shadow Points": "Your character's shadow points",
    "Shadow Scars": "Your character's shadow scars",

    # Conditions
    "Weary": "Weather or not your character is weary",
    "Miserable": "Weather or not your character is miserable",
    "Wounded": "Weather or not your character is wounded",
    "Injury": "How many more days you character will be wounded for"
}

editable_attributes = {
    "Name": "Your character's name",

    "Age": "Your character's age",
    "Treasure": "Your character's current treasure points",
    "Patron": "Your character's patron",

    "Distinctive Features": "Your character's distinctive features",

    # Attributes and Derived Stats
    "Strength": "Your character's strength rating",
    "Strength TN": "The TN for your character's Strength Skills",
    "Max Endurance": "Your character's maximum endurance",

    "Heart": "Your character's heart rating",
    "Heart TN": "The TN for your character's Heart Skills",
    "Max Hope": "Your character's maximum hope",

    "Wits": "Your character's wits rating",
    "Wits TN": "The TN for your character's Wits Skills",
    "Parry": "Your character's parry rating",

    # Skills
    "Awe": "Your character's awe skill level",
    "Athletics": "Your character's athletics skill level",
    "Awareness": "Your character's awareness skill level",
    "Hunting": "Your character's hunting skill level",
    "Song": "Your character's song skill level",
    "Craft": "Your character's craft skill level",

    "Enhearten": "Your character's enhearten skill level",
    "Travel": "Your character's travel skill level",
    "Insight": "Your character's insight skill level",
    "Healing": "Your character's healing skill level",
    "Courtesy": "Your character's courtesy skill level",
    "Battle": "Your character's battle skill level",

    "Persuade": "Your character's persuade skill level",
    "Stealth": "Your character's stealth skill level",
    "Scan": "Your character's scan skill level",
    "Explore": "Your character's explore skill level",
    "Riddle": "Your character's riddle skill level",
    "Lore": "Your character's lore skill level",

    "Favoured Skills": "A list of your character's favoured skills",

    # Combat Proficencies
    "Axes": "Your character's axes proficincey level",
    "Bows": "Your character's bows proficincey level",
    "Spears": "Your character's spears proficincey level",
    "Swords": "Your character's swords proficincey level",

    # Valour/Wisdom
    "Valour": "Your character's valour rating",
    "Rewards": "A list of your character's rewards",
    "Wisdom": "Your character's wisdom rating",
    "Virtues": "A list of your character's virtues",

    # Gear
    "Weapons": "A list of your character's weapons",
    "Armour": "Your character's armour",
    "Shield": "Your character's shield",
    "Headgear": "Your character's headgear",
    "Traveling Gear": "Your character's travelling gear",

    # Other
    "Adventure Points": "Your character's adventure points",
    "Skill Points": "Your character's skill points",
    "Fellowship Score": "Your character's fellowship score",

    # Endurance/Hope
    "Current Endurance": "Your character's current endurance",
    "Fatigue": "Your character's fatigue level",
    "Current Hope": "Your character's current hope",
    "Shadow Points": "Your character's shadow points",
    "Shadow Scars": "Your character's shadow scars",

    # Conditions
    "Wounded": "Weather or not your character is wounded",
    "Injury": "How many more days you character will be wounded for"
}

keys = list(viewable_attributes.keys())
keys.sort()
viewable_attributes = {key: viewable_attributes[key] for key in keys}

keys = list(editable_attributes.keys())
keys.sort()
editable_attributes = {key: editable_attributes[key] for key in keys}


def clear_console(active_character: Character = None):
    """Clears the console and prints the title. If a character object is passed, it will autosave that character."""
    os.system('cls' if os.name == 'nt' else 'clear')
    if active_character is not None:
        autosave(active_character)
    print(f"One Ring RPG Character Manager\n"
          f"Version: {version}\n"
          f"Enter 'help' at any time for a list of commands or 'exit' to quit\n\n")
    

def start_help():
    """Prints the commands available to someone who just started the program."""
    clear_console()
    print("Valid commands include: \n")
    for command, description in start_commands.items(): 
        print(f"{command}: {description}")
    print("\n")


def help():
    """Prints the commands available to someone who has an active character."""
    clear_console()
    print("Valid commands include:\n")
    for command, description in commands.items():
        print(f"{command}: {description}")
    print()


def create_character():
    active_character = character_creation.main()
    if input("Would you like to save and continue with this character? (y/n)").lower() == "y":
        save_character(active_character)
        clear_console(active_character)
        print(f"{active_character.name} successfully created and saved!")
        return active_character


def select_character_to_load(input_command: str):
    """Walks the user through selecting a character to load."""
    clear_console()
    while True:
        if input_command is None:
            print("Enter the name of the character you would like to load: ")
            input_command = input("> ").lower()
        if input_command == "exit":
            exit()
        elif input_command == "menu":
            clear_console()
            return
        elif input_command == "help":
            clear_console()
            print("Valid commands include: \n")
            print("exit: Exits the program.")
            print("menu: Returns to the main menu.")
            print("{character name}: Loads the character with that name.\n\n")
            input_command = None
        else:
            character_name = input_command
            try:
                active_character = load_character(f"{character_name}")
                break
            except FileNotFoundError:
                clear_console()
                print("No character with that name was found.\n\n")
                input_command = None
    clear_console(active_character)
    print(f"{active_character.name} successfully loaded!\n\n")
    return active_character


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


def save_current_character(active_character: Character):
    save_character(active_character)
    clear_console(active_character)
    print(f"{active_character.name} successfully saved!\n")


def show_attribute(active_character: Character, commands: list[str]):

    attribute = " ".join(commands[1:])

    if attribute == "":
        clear_console(active_character)
        print("Enter the attribute you would like to view: ")
        attribute = input("> ").lower()

    clear_console(active_character)
    match attribute:
        case "help":
            print(f"Valid attributes include:")
            for viewee, description in viewable_attributes.items():
                print(f"{viewee}: {description}")
            print("\n")

        case "name":
            print(f"{attribute}: {active_character.name}\n\n")
        case "culture" | "heroic culture" | "heroic_culture":
            print(f"{attribute}: {active_character.culture}\n\n")
        case "blessing" | "cultural blessing"| "cultural_blessing":
            print(f"{attribute}: {active_character.blessing}\n\n")
        case "calling":
            print(f"{attribute}: {active_character.calling}\n\n")
        case "age":
            print(f"{attribute}: {active_character.age}\n\n")
        case "standard of living" | "sol" | "standard_of_living":
            print(f"{attribute}: {active_character.standard_of_living}\n\n")
        case "treasure" | "treasure rating" | "treasrue points" | "treasure_rating" | "treasure_points":
            print(f"{attribute}: {active_character.treasure}\n\n")
        case "patron":
            print(f"{attribute}: {active_character.patron}\n\n")
        case "shadow path":
            print(f"{attribute}: {active_character.shadow_path}\n\n")
        case "distinctive features" | "features" | "distinctive_features":
            print(f"{attribute}: {active_character.distinctive_features}\n\n")
        case "flaws":
            print(f"{attribute}: {active_character.flaws}\n\n")

        case "strength" | "strength score" | "strength_score":
            print(f"{attribute}: {active_character.strength_score}\n\n")
        case "strength tn" | "strength_tn":
            print(f"{attribute}: {active_character.strength_tn}\n\n")
        case "max endurance" | "max_endurance":
            print(f"{attribute}: {active_character.max_endurance}\n\n")

        case "heart" | "heart score" | "heart_score":
            print(f"{attribute}: {active_character.heart_score}\n\n")
        case "heart tn" | "heart_tn":
            print(f"{attribute}: {active_character.heart_tn}\n\n")
        case "max hope" | "max_hope":
            print(f"{attribute}: {active_character.max_hope}\n\n")

        case "wits" | "wits score" | "wits_score":
            print(f"{attribute}: {active_character.wits_score}\n\n")
        case "wits tn" | "wits_tn":
            print(f"{attribute}: {active_character.wits_tn}\n\n")
        case "parry" | "parry rating" | "parry_rating":
            print(f"{attribute}: {active_character.parry}\n\n")

        case "awe" | "awe level" | "awe_level":
            print(f"{attribute}: {active_character.awe}\n\n")
        case "athletics" | "athletics level" | "athletics_level":
            print(f"{attribute}: {active_character.athletics}\n\n")
        case "awareness" | "awareness level" | "awareness_level":
            print(f"{attribute}: {active_character.awareness}\n\n")
        case "hunting" | "hunting level" | "hunting_level":
            print(f"{attribute}: {active_character.hunting}\n\n")
        case "song" | "song level" | "song_level":
            print(f"{attribute}: {active_character.song}\n\n")
        case "craft" | "craft level" | "craft_level":
            print(f"{attribute}: {active_character.craft}\n\n")
        case "enhearten" | "enhearten level" | "enhearten_level":
            print(f"{attribute}: {active_character.enhearten}\n\n")
        case "travel" | "travel level" | "travel_level":
            print(f"{attribute}: {active_character.travel}\n\n")
        case "insight" | "insight level" | "insight_level":
            print(f"{attribute}: {active_character.insight}\n\n")
        case "healing" | "healing level" | "healing_level":
            print(f"{attribute}: {active_character.healing}\n\n")
        case "courtesy" | "courtesy level" | "courtesy_level":
            print(f"{attribute}: {active_character.courtesy}\n\n")
        case "battle" | "battle level" | "battle_level":
            print(f"{attribute}: {active_character.battle}\n\n")
        case "persuade" | "persuade level" | "persuade_level":
            print(f"{attribute}: {active_character.persuade}\n\n")
        case "stealth" | "stealth level" | "stealth_level":
            print(f"{attribute}: {active_character.stealth}\n\n")
        case "scan" | "scan level" | "scan_level":
            print(f"{attribute}: {active_character.scan}\n\n")
        case "explore" | "explore level" | "explore_level":
            print(f"{attribute}: {active_character.explore}\n\n")
        case "riddle" | "riddle level" | "riddle_level":
            print(f"{attribute}: {active_character.riddle}\n\n")
        case "lore" | "lore level" | "lore_level":
            print(f"{attribute}: {active_character.lore}\n\n")
        case "favoured skills" | "favored skills":
            print(f"{attribute}: {active_character.favoured_skills}\n\n")

        case "axes" | "axes skill" | "axes_skill" | "axe" | "axe skill" | "axe_skill":
            print(f"{attribute}: {active_character.axes_skill}\n\n")
        case "bows" | "bows skill" | "bows_skill" | "bow" | "bow skill" | "bow_skill":
            print(f"{attribute}: {active_character.bows_skill}\n\n")
        case "spears" | "spears skill" | "spears_skill" | "spear" | "spear skill" | "spear_skill":
            print(f"{attribute}: {active_character.spears_skill}\n\n")
        case "swords" | "swords skill" | "swords_skill" | "sword" | "sword skill" | "sword_skill":
            print(f"{attribute}: {active_character.swords_skill}\n\n")

        case "valour":
            print(f"{attribute}: {active_character.valour}\n\n")
        case "rewards":
            print(f"{attribute}: {active_character.rewards}\n\n")
        case "wisdom":
            print(f"{attribute}: {active_character.wisdom}\n\n")
        case "virtues":
            print(f"{attribute}: {active_character.virtues}\n\n")

        case "weapons":
            print(f"{attribute}: {active_character.weapons}\n\n")
        case "armour" | "armor":
            print(f"{attribute}: {active_character.armour}\n\n")
        case "shield":
            print(f"{attribute}: {active_character.shield}\n\n")
        case "headgear":
            print(f"{attribute}: {active_character.headgear}\n\n")
        case "traveling gear" | "items":
            print(f"{attribute}: {active_character.traveling_gear}\n\n")

        case "adventure points" | "adventure_points" | "ap":
            print(f"{attribute}: {active_character.adventure_points}\n\n")
        case "skill points"| "skill_points" | "sp":
            print(f"{attribute}: {active_character.skill_points}\n\n")
        case "fellowship score" | "fellowship_score" | "fs":
            print(f"{attribute}: {active_character.fellowship_score}\n\n")

        case "current endurance" | "current_endurance":
            print(f"{attribute}: {active_character.current_endurance}\n\n")
        case "load":
            print(f"{attribute}: {active_character.load}\n\n")
        case "fatigue":
            print(f"{attribute}: {active_character.fatigue}\n\n")

        case "current hope" | "current_hope":
            print(f"{attribute}: {active_character.current_hope}\n\n")
        case "shadow":
            print(f"{attribute}: {active_character.shadow}\n\n")
        case "shadow points" | "shadow_points":
            print(f"{attribute}: {active_character.shadow_points}\n\n")
        case "shadow scars" | "shadow_scars":
            print(f"{attribute}: {active_character.shadow_scars}\n\n")

        case "weary":
            print(f"{attribute}: {active_character.is_weary}\n\n")
        case "miserable":
            print(f"{attribute}: {active_character.is_miserable}\n\n")
        case "wounded":
            print(f"{attribute}: {active_character.is_wounded}\n\n")
        case "injury":
            print(f"{attribute}: {active_character.injury}\n\n")
            
        case _:
            if attribute in viewable_attributes.keys():
                print(f"***THIS IS AN ERROR. PLEASE REPORT TO THE DEVELOPER WITH THE FOLLOWING CODE***"
                      f"***{attribute} is in viewable_attributes but match case in show_attribute didn't catch it***\n")
            else:
                print(f"Invalid attribute: {attribute}\n\n")
            

def set_attribute(active_character: Character, commands: list[str]):
    clear_console(active_character)

    

        
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
