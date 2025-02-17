from character import Character, save_character, load_character
from gear import Weapons, Armours, Shields, Headgears
from boons import Virtue, Reward
import os, sys, random, character_creation, pickle, statistics


version = "2.02"


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
    "revert": "Reverts the character to the last manually saved state.",
    "update": "Updates your character to the current version"
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

    "Favoured Skills": "A list of your character's favoured skills",

    "Skills": "A list of your character's skill levels",

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


STRENGTH_SKILLS = [
    "awe",
    "athletics",
    "awareness",
    "hunting",
    "song",
    "craft"
]

HEART_SKILLS = [
    "enhearten",
    "travel",
    "insight",
    "healing",
    "courtesy",
    "battle"
]

WITS_SKILLS = [
    "persuade",
    "stealth",
    "scan",
    "explore",
    "riddle",
    "lore"
]


keys = list(viewable_attributes.keys())
keys.sort()
viewable_attributes = {key: viewable_attributes[key] for key in keys}

keys = list(editable_attributes.keys())
keys.sort()
editable_attributes = {key: editable_attributes[key] for key in keys}

user_translator = {
    # name
    "exit": "exit",

    "menu": "menu",

    "help": "help",

    "name": "name",

    "culture":        "culture", 
    "heroic_culture": "culture",

    "blessing":          "blessing", 
    "cultural_blessing": "blessing",

    "calling": "calling",

    "age": "age",

    "sol":                "standard_of_living", 
    "standard_of_living": "standard_of_living",

    "treasure":        "treasure", 
    "treasure_rating": "treasure", 
    "treasure_points": "treasure",

    "patron": "patron",

    "shadow_path": "shadow_path",

    "distinctive_features": "distinctive_features", 
    "features":             "distinctive_features", 
    "feature":              "distinctive_features",

    "flaws": "flaws",


    # strength 
    "strength_score" : "strength_score",
    "strength" :       "strength_score", 
    "str":             "strength_score", 

    "strength_tn" : "strength_tn",
    "str tn":       "strength_tn", 
    
    "max_endurance": "max_endurance", 

    # heart
    "heart_score": "heart_score",
    "heart":       "heart_score",
    "hrt":         "heart_score",

    "heart_tn": "heart_tn",
    "hrt tn":   "heart_tn",

    "max_hope": "max_hope",

    # wits
    "wits_score": "wits_score",
    "wits":       "wits_score",
    "wts":        "wits_score",

    "wits_tn": "wits_tn",
    "wts_tn":  "wits_tn",

    "parry": "parry",


    # Skills
    "awe":             "awe",
    "awe_level":       "awe",
    "awe_skill":       "awe",
    "awe_skill_level": "awe",

    "athletics":             "athletics",
    "athletics_level":       "athletics",
    "athletics_skill":       "athletics",
    "athletics_skill_level": "athletics",

    "awareness":             "awareness",
    "awareness_level":       "awareness",
    "awareness_skill":       "awareness",
    "awareness_skill_level": "awareness",

    "hunting":             "hunting",
    "hunting_level":       "hunting",
    "hunting_skill":       "hunting",
    "hunting_skill_level": "hunting",

    "song":             "song",
    "song_level":       "song",
    "song_skill":       "song",
    "song_skill_level": "song",

    "craft":             "craft",
    "craft_level":       "craft",
    "craft_skill":       "craft",
    "craft_skill_level": "craft",


    "enhearten":             "enhearten",
    "enhearten_level":       "enhearten",
    "enhearten_skill":       "enhearten",
    "enhearten_skill_level": "enhearten",

    "travel":             "travel",
    "travel_level":       "travel",
    "travel_skill":       "travel",
    "travel_skill_level": "travel",

    "insight":             "insight",
    "insight_level":       "insight",
    "insight_skill":       "insight",
    "insight_skill_level": "insight",

    "healing":             "healing",
    "healing_level":       "healing",
    "healing_skill":       "healing",
    "healing_skill_level": "healing",

    "courtesy":             "courtesy",
    "courtesy_level":       "courtesy",
    "courtesy_skill":       "courtesy",
    "courtesy_skill_level": "courtesy",

    "battle":             "battle",
    "battle_level":       "battle",
    "battle_skill":       "battle",
    "battle_skill_level": "battle",


    "persuade":             "persuade",
    "persuade_level":       "persuade",
    "persuade_skill":       "persuade",
    "persuade_skill_level": "persuade",

    "stealth":             "stealth",
    "stealth_level":       "stealth",
    "stealth_skill":       "stealth",
    "stealth_skill_level": "stealth",

    "scan":             "scan",
    "scan_level":       "scan",
    "scan_skill":       "scan",
    "scan_skill_level": "scan",

    "explore":             "explore",
    "explore_level":       "explore",
    "explore_skill":       "explore",
    "explore_skill_level": "explore",

    "riddle":             "riddle",
    "riddle_level":       "riddle",
    "riddle_skill":       "riddle",
    "riddle_skill_level": "riddle",

    "lore":             "lore",
    "lore_level":       "lore",
    "lore_skill":       "lore",
    "lore_skill_level": "lore",

    "favoured_skills": "favoured_skills",
    "favored_skills":  "favoured_skills",

    "skills": "skills",


    # Combat Proficencies
    "axes_skill": "axes_skill",
    "axe_skill":  "axes_skill",
    "axe" :       "axes_skill",
    "axes":       "axes_skill",

    "bows_skill": "bows_skill",
    "bow_skill":  "bows_skill",
    "bow" :       "bows_skill",
    "bows":       "bows_skill",

    "spears_skill": "spears_skill",
    "spear_skill":  "spears_skill",
    "spear" :       "spears_skill",
    "spears":       "spears_skill",

    "swords_skill": "swords_skill",
    "sword_skill":  "swords_skill",
    "sword" :       "swords_skill",
    "swords":       "swords_skill",


    # Valour/Wisdom
    "valour": "valour",

    "rewards": "rewards",

    "wisdom": "wisdom",

    "virtues": "virtues",


    # Gear
    "weapons": "weapons",
    "weapon": "weapons",

    "armour": "armour",
    "armor": "armour",

    "shield": "shield",

    "headgear": "headgear",

    "traveling_gear": "traveling_gear",
    "travel_gear":    "traveling_gear",
    "tg":             "traveling_gear",
    "items":          "traveling_gear",


    # Other
    "adventure_points": "adventure_points",
    "ap":               "adventure_points",

    "skill_points": "skill_points",
    "sp":           "skill_points",

    "fellowship_score":  "fellowship_score",
    "fs":                "fellowship_score",
    "fellowship_points": "fellowship_score",
    "fp":                "fellowship_score",


    # Endurance/Hope
    "current_endurance": "current_endurance",

    "load": "load",

    "fatigue": "fatigue",

    "current_hope": "current_hope",

    "shadow": "shadow",

    "shadow_points": "shadow_points",

    "shadow_scars": "shadow_scars",


    # Conditions
    "weary":    "weary",
    "is_weary": "weary",

    "miserable":    "miserable",
    "is_miserable": "miserable",

    "wounded":    "wounded",
    "is_wounded": "wounded",

    "injury": "injury",

    "all": "all"
}


def clear_console():
    """Clears the console and prints the title. If a character object is passed, it will autosave that character."""
    os.system('cls' if os.name == 'nt' else 'clear')
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
        clear_console()
        print(f"{active_character.name} successfully created and saved!")
        return active_character


def select_character_to_load(commands: list[str]):
    """Walks the user through selecting a character to load."""
    try:
        character_name = commands[1]
    except IndexError:
        clear_console()
        print("Enter the name of the character you would like to load: ")
        character_name = input("> ").lower()


    if character_name == "exit":
        exit()
    elif character_name == "menu":
        clear_console()
        return
    elif character_name == "help":
        clear_console()
        print("Valid commands include: \n")
        print("exit: Exits the program.")
        print("menu: Returns to the main menu.")
        print("{character name}: Loads the character with that name.\n\n")
    else:
        try:
            active_character = load_character(f"{character_name}")
        except FileNotFoundError:
            clear_console()
            print("No character with that name was found.\n\n")
        else:
            update_character(active_character)
            clear_console()
            print(f"{active_character.name} successfully loaded!\n\n")
            return active_character


def weapon_names(active_character: Character):
    weapon_names = []
    for weapon in active_character.weapons:
        weapon_names.append(weapon.name)
    return weapon_names


def reward_names(active_character: Character):
    reward_names = []
    for reward in active_character.rewards:
        reward_names.append(reward.name)
    return reward_names


def virtue_names(active_character: Character):
    virtue_names = []
    for virtue in active_character.virtues:
        virtue_names.append(virtue.name)
    return virtue_names


def save_current_character(active_character: Character):
    save_character(active_character)
    clear_console()
    print(f"{active_character.name} successfully saved!\n\n")


def show_attribute(active_character: Character, commands: list[str]):
    try:
        attribute = commands[1]
    except IndexError:
        clear_console()
        print("Enter the attribute you would like to view: ")
        attribute = input("> ").lower()


    clear_console()
    try:
        match user_translator[attribute]:
            case "help":
                print(f"Valid attributes include:")
                for viewee, description in viewable_attributes.items():
                    print(f"{viewee}: {description}")
                print("\n")
            case "name":
                print(f"{attribute}: {active_character.name}\n\n")
            case "culture":
                print(f"{attribute}: {active_character.culture}\n\n")
            case "blessing":
                print(f"{attribute}: {active_character.blessing}\n\n")
            case "calling":
                print(f"{attribute}: {active_character.calling}\n\n")
            case "age":
                print(f"{attribute}: {active_character.age}\n\n")
            case "standard_of_living":
                print(f"{attribute}: {active_character.standard_of_living}\n\n")
            case "treasure":
                print(f"{attribute}: {active_character.treasure}\n\n")
            case "patron":
                print(f"{attribute}: {active_character.patron}\n\n")
            case "shadow_path":
                print(f"{attribute}: {active_character.shadow_path}\n\n")
            case "distinctive_features":
                print(f"{attribute}: {active_character.distinctive_features}\n\n")
            case "flaws":
                print(f"{attribute}: {active_character.flaws}\n\n")

            case "strength_score":
                print(f"{attribute}: {active_character.strength_score}\n\n")
            case "strength_tn":
                print(f"{attribute}: {active_character.strength_tn}\n\n")
            case "max_endurance":
                print(f"{attribute}: {active_character.max_endurance}\n\n")

            case "heart_score":
                print(f"{attribute}: {active_character.heart_score}\n\n")
            case "heart_tn":
                print(f"{attribute}: {active_character.heart_tn}\n\n")
            case "max_hope":
                print(f"{attribute}: {active_character.max_hope}\n\n")

            case "wits_score":
                print(f"{attribute}: {active_character.wits_score}\n\n")
            case "wits_tn":
                print(f"{attribute}: {active_character.wits_tn}\n\n")
            case "parry":
                print(f"{attribute}: {active_character.parry}\n\n")

            case "awe":
                print(f"{attribute}: {active_character.awe}\n\n")
            case "athletics":
                print(f"{attribute}: {active_character.athletics}\n\n")
            case "awareness":
                print(f"{attribute}: {active_character.awareness}\n\n")
            case "hunting":
                print(f"{attribute}: {active_character.hunting}\n\n")
            case "song":
                print(f"{attribute}: {active_character.song}\n\n")
            case "craft":
                print(f"{attribute}: {active_character.craft}\n\n")
            case "enhearten":
                print(f"{attribute}: {active_character.enhearten}\n\n")
            case "travel":
                print(f"{attribute}: {active_character.travel}\n\n")
            case "insight":
                print(f"{attribute}: {active_character.insight}\n\n")
            case "healing":
                print(f"{attribute}: {active_character.healing}\n\n")
            case "courtesy":
                print(f"{attribute}: {active_character.courtesy}\n\n")
            case "battle":
                print(f"{attribute}: {active_character.battle}\n\n")
            case "persuade":
                print(f"{attribute}: {active_character.persuade}\n\n")
            case "stealth":
                print(f"{attribute}: {active_character.stealth}\n\n")
            case "scan":
                print(f"{attribute}: {active_character.scan}\n\n")
            case "explore":
                print(f"{attribute}: {active_character.explore}\n\n")
            case "riddle":
                print(f"{attribute}: {active_character.riddle}\n\n")
            case "lore":
                print(f"{attribute}: {active_character.lore}\n\n")
            case "favoured_skills":
                print(f"{attribute}: {active_character.favoured_skills}\n\n")
            case "skills":
                for skill, level in active_character.skill_levels.items():
                    print(f"{skill}: {level}")
                print("\n")

            case "axes_skill":
                print(f"{attribute}: {active_character.axes_skill}\n\n")
            case "bows_skill":
                print(f"{attribute}: {active_character.bows_skill}\n\n")
            case "spears_skill":
                print(f"{attribute}: {active_character.spears_skill}\n\n")
            case "swords_skill":
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
            case "armour":
                print(f"{attribute}: {active_character.armour}\n\n")
            case "shield":
                print(f"{attribute}: {active_character.shield}\n\n")
            case "headgear":
                print(f"{attribute}: {active_character.headgear}\n\n")
            case "traveling_gear":
                print(f"{attribute}: {active_character.traveling_gear}\n\n")

            case "adventure_points":
                print(f"{attribute}: {active_character.adventure_points}\n\n")
            case "skill_points":
                print(f"{attribute}: {active_character.skill_points}\n\n")
            case "fellowship_score":
                print(f"{attribute}: {active_character.fellowship_score}\n\n")

            case "current_endurance":
                print(f"{attribute}: {active_character.current_endurance}\n\n")
            case "load":
                print(f"{attribute}: {active_character.load}\n\n")
            case "fatigue":
                print(f"{attribute}: {active_character.fatigue}\n\n")

            case "current_hope":
                print(f"{attribute}: {active_character.current_hope}\n\n")
            case "shadow":
                print(f"{attribute}: {active_character.shadow}\n\n")
            case "shadow_points":
                print(f"{attribute}: {active_character.shadow_points}\n\n")
            case "shadow_scars":
                print(f"{attribute}: {active_character.shadow_scars}\n\n")

            case "weary":
                print(f"{attribute}: {active_character.is_weary}\n\n")
            case "miserable":
                print(f"{attribute}: {active_character.is_miserable}\n\n")
            case "wounded":
                print(f"{attribute}: {active_character.is_wounded}\n\n")
            case "injury":
                print(f"{attribute}: {active_character.injury}\n\n")

            case "all":
                print(active_character)
            
            case _:
                print(f"***THIS IS AN ERROR. PLEASE REPORT TO THE DEVELOPER WITH THE FOLLOWING CODE***\n"
                      f"***{attribute} is in user_translator but match case in show_attribute didn't catch it***\n")
    except KeyError:
        print(f"'{attribute}' is not a valid attribute.\n\n")
                       

def set_attribute(active_character: Character, commands: list[str]):

    # getting the attribute
    try:
        attribute = commands[1]
    except IndexError:
        clear_console()
        print("Enter the attribute you would like to set: ")
        attribute = input("> ").lower()

    # checking to see if the attribute given is valid
    try:
        user_translator[attribute]
    except KeyError:
        clear_console()
        print(f"'{attribute}' is not a valid attribute.\n\n")
        return None

    clear_console()

    match user_translator[attribute]:
        case "help":
            print(f"Valid attributes include:\n")
            for viewee, description in editable_attributes.items():
                print(f"{viewee}: {description}")
            print("\n")

        case "menu":
            clear_console()
            return None

        case "name":
            clear_console()
            print(f"Enter the new name for your character: ")
            value = input("> ")
            active_character.name = value
            clear_console()
            print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "age":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Age must be an integer.\n\n")
            else:
                active_character.age = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "treasure":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Treasure must be an integer.\n\n")
            else:
                active_character.treasure = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "patron":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to: ")
            value = input("> ")
            active_character.patron = value
            clear_console()
            print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "distinctive_features":
            print("Would you like to add or remove a distinctive feature? (add/remove): ")
            answer = input("> ").lower()
            match answer:
                case "add":
                    clear_console()
                    print(f"Enter the name of the distinctive feature you would like to add: ")
                    value = input("> ")
                    active_character.distinctive_features.append(value)
                    clear_console()
                    print(f"{value} successfully added to your list of distinctive features.\n\n")
                case "remove":
                    clear_console()
                    print(f"Enter the name of the distinctive feature you would like to remove: ")
                    value = input("> ")
                    try:
                        active_character.distinctive_features.remove(value)
                        clear_console()
                        print(f"{value} successfully removed from your list of distinctive features.\n\n")
                    except ValueError:
                        print(f"{value} is not in your list of distinctive features.\n\n")
                case _:
                    print("Invalid input.\n\n")

        case "strength_score":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Strength score must be an integer.\n\n")
            else:
                active_character.strength_score = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "strength_tn":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Strength TN must be an integer.\n\n")
            else:
                active_character.strength_tn = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "max_endurance":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Max endurance must be an integer.\n\n")
            else:
                active_character.max_endurance = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")


        case "heart_score":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Heart score must be an integer.\n\n")
            else:
                active_character.heart_score = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "heart_tn":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Heart TN must be an integer.\n\n")
            else:
                active_character.heart_tn = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "max_hope":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ") 
            try:
                value = int(value)
            except ValueError:
                print("Max hope must be an integer.\n\n")
            else:
                active_character.max_hope = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")


        case "wits_score":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Wits score must be an integer.\n\n")
            else:
                active_character.wits_score = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "wits_tn":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Wits TN must be an integer.\n\n")
            else:
                active_character.wits_tn = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")

        case "parry":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Parry must be an integer.\n\n")
            else:
                active_character.parry = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")


        case "awe":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Awe must be an integer.\n\n")
            else:
                active_character.awe = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "athletics":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Athletics must be an integer.\n\n")
            else:
                active_character.athletics = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "awareness":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Awareness must be an integer.\n\n")
            else:
                active_character.awareness = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "hunting":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Hunting must be an integer.\n\n")
            else:
                active_character.hunting = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "song":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Song must be an integer.\n\n")
            else:
                active_character.song = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "craft":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Craft must be an integer.\n\n")
            else:
                active_character.craft = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "enhearten":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Enhearten must be an integer.\n\n")
            else:
                active_character.enhearten = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "travel":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Travel must be an integer.\n\n")
            else:
                active_character.travel = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "insight":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Insight must be an integer.\n\n")
            else:
                active_character.insight = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "healing":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Healing must be an integer.\n\n")
            else:
                active_character.healing = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "courtesy":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Courtesy must be an integer.\n\n")
            else:
                active_character.courtesy = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "battle":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Battle must be an integer.\n\n")
            else:
                active_character.battle = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "persuade":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Persuade must be an integer.\n\n")
            else:
                active_character.persuade = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "stealth":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Stealth must be an integer.\n\n")
            else:
                active_character.stealth = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "scan":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Scan must be an integer.\n\n")
            else:
                active_character.scan = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "explore":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Explore must be an integer.\n\n")
            else:
                active_character.explore = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "riddle":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Riddle must be an integer.\n\n")
            else:
                active_character.riddle = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "lore":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Lore must be an integer.\n\n")
            else:
                active_character.lore = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "favoured_skills":
            print("Would you like to add or remove a favoured skill? (add/remove): ")
            answer = input("> ").lower()
            match answer:
                case "add":
                    clear_console()
                    print(f"Enter the name of the skill you would like to add to you list of favoured skills: ")
                    value = input("> ")
                    active_character.favoured_skills.append(value)
                    clear_console()
                    print(f"'{value}' successfully added to your list of favoured skills.\n\n")
                case "remove":
                    clear_console()
                    print(f"Enter the name of the skill you would like to remove from you list of favoured skills: ")
                    value = input("> ")
                    try:
                        active_character.favoured_skills.remove(value)
                        clear_console()
                        print(f"'{value}' successfully removed from your list of favoured skills.\n\n")
                    except ValueError:
                        clear_console()
                        print(f"{value} is not in your list of favoured skills.\n\n")
                case _:
                    clear_console()
                    print("Invalid input.\n\n")\
       

        case "axes_skill":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Axes skill must be an integer.\n\n")
            else:
                active_character.combat_proficiencies["axes"] = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "bows_skill":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Bows skill must be an integer.\n\n")
            else:
                active_character.combat_proficiencies["bows"] = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "spears_skill":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Spears skill must be an integer.\n\n")
            else:
                active_character.combat_proficiencies["spears"] = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "swords_skill":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Swords skill must be an integer.\n\n")
            else:
                active_character.combat_proficiencies["swords"] = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        

        case "valour":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Valour must be an integer.\n\n")
            else:
                active_character.valour = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "rewards":
            print("Would you like to add, remove, or modify a reward? (add/remove/modify): ")
            answer = input("> ").lower()
            match answer:
                case "add":
                    new_reward = Reward()

                    clear_console()
                    print(f"Enter the name of the reward you would like to add to your list of rewards: ")
                    new_reward.name = input("> ")

                    clear_console()
                    print(f"Enter the effect of the reward you would like to add to your list of rewards: ")
                    new_reward.effect = input("> ")

                    active_character.rewards.append(new_reward)
                    clear_console()
                    print(f"'{new_reward.name}' successfully added to your list of '{attribute}'.\n\n")
                case "remove":
                    clear_console()
                    print(f"Enter the name of the reward you would like to remove from your list of rewards: ")
                    value = input("> ")
                    if value in reward_names(active_character):
                        for reward in active_character.rewards:
                            if reward.name == value:
                                active_character.rewards.remove(reward)
                                clear_console()
                                print(f"'{value}' successfully removed from your list of '{attribute}'.\n\n")
                    else:
                        print(f"'{value}' is not in your list of rewards.\n\n")
                case "modify":
                    clear_console()
                    print(f"Enter the name of the reward you would like to modify from your list of rewards: ")
                    name = input("> ")
                    if name in reward_names(active_character):
                        clear_console()
                        print(f"Enter the attribute of {name} you would like to modify: ")
                        match input("> ").lower():
                            case "name":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s name to: ")
                                active_character.rewards_by_name(name).name = input("> ")
                                clear_console()
                                print(f"{name}'s name successfully changed to '{active_character.rewards_by_name(name).name}'.\n\n")
                            case "effect":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s effect to: ")
                                active_character.rewards_by_name(name).effect = input("> ")
                                clear_console()
                                print(f"{name}'s effect successfully changed to '{active_character.rewards_by_name(name).effect}'.\n\n")
                            case _:
                                clear_console()
                                print(f"'{name}' is not a valid attribute of a reward.\n\n")
                                return                            
                    else:
                        clear_console()
                        print(f"{name}' is not in your list of rewards.\n\n")
                        return
                case _:
                    clear_console()
                    print("Invalid input.\n\n")
        
        case "wisdom":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Wisdom must be an integer.\n\n")
            else:
                active_character.wisdom = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "virtues":
            print("Would you like to add, remove, or modify a virtue? (add/remove/modify): ")
            answer = input("> ").lower()
            match answer:
                case "add":
                    new_virtue = Virtue()

                    clear_console()
                    print(f"Enter the name of the virtue you would like to add to your list of virtues: ")
                    new_virtue.name = input("> ")

                    clear_console()
                    print(f"Enter the effect of the virtue you would like to add to your list of virtues: ")
                    new_virtue.effect = input("> ")

                    active_character.virtues.append(new_virtue)
                    clear_console()
                    print(f"'{new_virtue.name}' successfully added to your list of '{attribute}'.\n\n")
                case "remove":
                    clear_console()
                    print(f"Enter the name of the virtue you would like to remove from your list of virtues: ")
                    value = input("> ")
                    if value in virtue_names(active_character):
                        for virtue in active_character.virtues:
                            if virtue.name == value:
                                active_character.virtues.remove(virtue)
                                clear_console()
                                print(f"'{value}' successfully removed from your list of '{attribute}'.\n\n")
                    else:
                        print(f"'{value}' is not in your list of virtues.\n\n")
                case "modify":
                    clear_console()
                    print(f"Enter the name of the virtue you would like to modify from your list of virtues: ")
                    name = input("> ")
                    if name in virtue_names(active_character):
                        clear_console()
                        print(f"Enter the attribute of {name} you would like to modify: ")
                        match input("> ").lower():
                            case "name":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s name to: ")
                                active_character.virtues_by_name(name).name = input("> ")
                                clear_console()
                                print(f"{name}'s name successfully changed to '{active_character.virtues_by_name(name).name}'.\n\n")
                            case "effect":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s effect to: ")
                                active_character.virtues_by_name(name).effect = input("> ")
                                clear_console()
                                print(f"{name}'s effect successfully changed to '{active_character.virtues_by_name(name).effect}'.\n\n")
                            case _:
                                clear_console()
                                print(f"'{name}' is not a valid attribute of a virtue.\n\n")
                                return
                    else:
                        clear_console()
                        print(f"{name}' is not in your list of virtues.\n\n")
                        return
                case _:
                    clear_console()
                    print("Invalid input.\n\n")
        

        case "weapons":
            print("Would you like to add, remove, or modify a weapon? (add/remove/modify): ")
            answer = input("> ").lower()
            match answer:
                case "add":
                    clear_console()
                    print(f"Enter the name of the weapon you would like to add to your list of weapons: ")
                    value = input("> ")
                    if value in Weapons.names():
                        active_character.weapons.append(Weapons.by_name(value))
                        clear_console()
                        print(f"'{value}' successfully added to your list of '{attribute}'.\n\n")
                    else:
                        clear_console()
                        print(f"'{value}' is not a valid weapon.\n\n")
                case "remove":
                    clear_console()
                    print(f"Enter the name of the weapon you would like to remove from your list of weapons: ")
                    value = input("> ")
                    if value in weapon_names(active_character):
                        for weapon in active_character.weapons:
                            if weapon.name == value:
                                active_character.weapons.remove(weapon)
                                clear_console()
                                print(f"'{value}' successfully removed from your list of '{attribute}'.\n\n")
                    else:
                        print(f"'{value}' is not in your list of weapons.\n\n")
                case "modify":
                    clear_console()
                    print(f"Enter the name of the weapon you would like to modify: ")
                    name = input("> ")
                    if name in weapon_names(active_character):
                        clear_console()
                        print(f"Enter the attribute of {name} you would like to modify: ")
                        match input("> ").lower():
                            case "name":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s name to: ")
                                new_name = input("> ")
                                active_character.weapons_by_name(name).name = new_name
                                clear_console()
                                print(f"{name}'s name successfully changed to '{active_character.weapons_by_name(new_name).name}'.\n\n")
                            case "damage":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s damage to: ")
                                active_character.weapons_by_name(name).damage = input("> ")
                                print(f"{name}'s damage successfully changed to '{active_character.weapons_by_name(name).damage}'.\n\n")
                            case "injury":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s injury to: ")
                                active_character.weapons_by_name(name).injury = input("> ")
                                print(f"{name}'s injury successfully changed to '{active_character.weapons_by_name(name).injury}'.\n\n")
                            case "load":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s load to: ")
                                active_character.weapons_by_name(name).load = input("> ")
                                print(f"{name}'s load successfully changed to '{active_character.weapons_by_name(name).load}'.\n\n")
                            case "notes":
                                clear_console()
                                print(f"Enter what you would like to change {name}'s notes to: ")
                                active_character.weapons_by_name(name).notes = input("> ")
                                print(f"{name}'s notes successfully changed to '{active_character.weapons_by_name(name).notes}'.\n\n")
                            case _:
                                clear_console()
                                print(f"'{name}' is not a valid attribute of a weapon.\n\n")
                                return
                    else:
                        clear_console()
                        print(f"'{name}' is not in your list of weapons.\n\n")
                        return
                case _:
                    print("Invalid input.\n\n")
        
        case "armour":
            print("Would you like to remove or replace armour? (remove/replace): ")
            answer = input("> ").lower()
            match answer:
                case "remove":
                    active_character.armour = None
                case "replace":
                    clear_console()
                    print(f"Enter the name of the armour you would like to replace your current armour with: ")
                    value = input("> ")
                    active_character.armour = Armours.by_name(value)
                    clear_console()
                    print(f"'{attribute}' successfully set to '{value}'.\n\n")
                case _:
                    print("Invalid Input\n\n")
        
        case "shield":
            print("Would you like to remove or replace a shield? (remove/replace): ")
            answer = input("> ").lower()
            match answer:
                case "remove":
                    active_character.shield = None
                case "replace":
                    clear_console()
                    print(f"Enter the name of the shield you would like to replace your current shield with: ")
                    value = input("> ")
                    active_character.shield = Shields.by_name(value)
                    print(f"'{attribute}' successfully set to '{value}'.\n\n")
                case _:
                    print("Invalid Input\n\n")
        
        case "headgear":
            print("Would you like to remove or replace headgear? (remove/replace): ")
            answer = input("> ").lower()
            match answer:
                case "remove":
                    active_character.headgear = None
                case "replace":
                    clear_console()
                    print(f"Enter the name of the headgear you would like to replace your current headgear with: ")
                    value = input("> ")
                    active_character.headgear = Headgears.by_name(value)
                    print(f"'{attribute}' successfully set to '{value}'.\n\n")
                case _:
                    print("Invalid Input\n\n")
        
        case "traveling_gear":
            print("Would you like to add or remove a piece of traveling gear? (add/remove): ")
            answer = input("> ").lower()
            match answer:
                case "add":
                    clear_console()
                    print(f"Enter the name of the traveling gear you would like to add to your list of traveling gear")
                    value = input("> ")
                    if active_character.traveling_gear == None:
                        active_character.traveling_gear = []
                    active_character.traveling_gear.append(value)
                    clear_console()
                    print(f"'{value}'successfully added to your list of '{attribute}'.\n\n")
                case "remove":
                    clear_console()
                    print(f"Enter the name of the traveling gear you would like to remove from your list of traveling gear")
                    value = input("> ")
                    try:
                        active_character.traveling_gear.remove(value)
                        clear_console()
                        print(f"'{value}'successfully removed from your list of '{attribute}'.\n\n")
                    except ValueError:
                        print(f"{value} is not in your list of traveling gear.\n\n")
                case _:
                    print("Invalid input.\n\n")
        

        case "adventure_points":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Adventure points must be an integer.\n\n")
            else:
                active_character.adventure_points = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "skill_points":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Skill points must be an integer.\n\n")
            else:
                active_character.skill_points = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "fellowship_score":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Fellowship score must be an integer.\n\n")
            else:
                active_character.fellowship_score = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        

        case "current_endurance":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Current endurance must be an integer.\n\n")
            else:
                active_character.current_endurance = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
                
        case "fatigue":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Fatigue must be an integer.\n\n")
            else:
                active_character.fatigue = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        

        case "current_hope":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Current hope must be an integer.\n\n")
            else:
                active_character.current_hope = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
                
        case "shadow_points":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Shadow points must be an integer.\n\n")
            else:
                active_character.shadow_points = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        case "shadow_scars":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Shadow scars must be an integer.\n\n")
            else:
                active_character.shadow_scars = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        

        case "wounded":
            print(f"If you would like to make your character wounded, enter 'True'. If you would like to make your character not wounded, enter 'False': ")
            value = input("> ")
            if value in ["True", "true", "TRUE"]:
                value = True
                active_character.is_wounded = value
                clear_console()
                print(f"{active_character.name} is now wounded.\n\n")
            elif value in ["False", "false", "FALSE"]:
                value = False
                active_character.is_wounded = value
                clear_console()
                print(f"{active_character.name} is no longer wounded.\n\n")
            else:
                print("Wounded must be a boolean (either TRUE or FALSE).\n\n")
        
        case "injury":
            clear_console()
            print(f"Enter the value you would like to set '{attribute}' to. It must be an integer: ")
            value = input("> ")
            try:
                value = int(value)
            except ValueError:
                print("Injury must be an integer.\n\n")
            else:
                active_character.injury = value
                clear_console()
                print(f"'{attribute}' successfully set to '{value}'.\n\n")
        
        
        case _:
            clear_console()
            print(f"***THIS IS AN ERROR. PLEASE REPORT TO THE DEVELOPER WITH THE FOLLOWING CODE***\n"
                f"***{attribute} is in user_translator but match case in show_attribute didn't catch it***\n")
            
    autosave(active_character)


def roll(skill_level: int, is_favoured: bool = False):
    if is_favoured:
        feat_1 = random.randint(0, 11)
        feat_2 = random.randint(0, 11)
        if feat_1 > feat_2:
            feat_result = feat_1
        else:
            feat_result = feat_2
    else:
        feat_result = random.randint(0, 11)

    success_results = []
    for c in range(skill_level):
        success_results.append(random.randint(1, 6))

    return feat_result, success_results

    
def roll_attribute(active_character: Character, commands: list[str]):
    
    # getting the number of dice to roll
    try:
        skill_level = commands[1]
    except IndexError:
        clear_console()
        print("Enter the number of success dice you would like to roll: ")
        skill_level = input("> ")

    # making sure it's an int
    try:
        skill_level = int(skill_level)
    except ValueError:
        clear_console()
        print("Skill level must be an integer.\n\n")
        return
    
    # getting weather or not it's favoured
    try:
        is_favoured = commands[2]
    except IndexError:
        clear_console()
        print("Enter whether the roll is favoured (True or False): ")
        is_favoured = input("> ")
    
    
    if is_favoured not in ["True", "true", "TRUE", "False", "false", "FALSE"]:
        clear_console()
        print("Is favoured must be a boolean (either TRUE or FALSE).\n\n")
        return
    
    match is_favoured:
        case "True":
            is_favoured = True
        case "true":
            is_favoured = True
        case "TRUE":
            is_favoured = True
        case "False":
            is_favoured = False
        case "false":
            is_favoured = False
        case "FALSE":
            is_favoured = False

    feat_result, success_results = roll(int(skill_level), bool(int(is_favoured)))

    clear_console()
    if feat_result == 0:
        feat_result = "Eye of Sauron"
        print(f"Feat Result: {feat_result}")
        print(f"Success Results: {success_results}")
        print(f"Total: {sum(success_results)}\n\n")

    elif feat_result == 11:
        feat_result = "G-Rune"
        print(f"Feat Result: {feat_result}")
        print(f"Success Results: {success_results}")
        print(f"Total: Atuomatic Success\n\n")
        
    else:
        print(f"Feat Result: {feat_result}")
        print(f"Success Results: {success_results}")
        print(f"Total: {sum(success_results) + feat_result}\n\n")


def autosave(active_character: Character):
    with open(f"{active_character.name}_autosave.pickle", 
    "wb") as file:
        pickle.dump(active_character, file)


def update_character(active_character: Character):
    clear_console()

    try:
        active_character.traveling_gear
    except:
        active_character.traveling_gear = []

    for skill in active_character.favoured_skills:
        if type(skill) == str:
                pass
        else:
            active_character.favoured_skills = [active_character.favoured_skills[0], active_character.favoured_skills[1][0], active_character.favoured_skills[1][1]]


    try:
        active_character.favoured_skills = [active_character.favoured_skills[0][0], active_character.favoured_skills[0][1][0], active_character.favoured_skills[0][1][1]]
    except IndexError:
        pass
    
    try:
        if type(active_character.virtues[0]) == str:
            try:
                new_virtue = Virtue()
                old_virtues = active_character.virtues
                active_character.virtues = []
                for virtue in old_virtues:
                    new_virtue.name = virtue
                    active_character.virtues.append(new_virtue)

                new_reward = Reward()
                old_rewards = active_character.rewards
                active_character.rewards = []
                for reward in old_rewards:
                    new_reward.name = reward
                    active_character.rewards.append(new_reward)
            except:
                pass
    except:
        pass

    old_combat_proficencies = active_character.combat_proficiencies
    active_character.combat_proficiencies = {}
    active_character.combat_proficiencies.update({'axes': old_combat_proficencies.get('axes'),
                                                   'bows': old_combat_proficencies.get('bows'),
                                                   'spears': old_combat_proficencies.get('spears'),
                                                   'swords': old_combat_proficencies.get('swords')})
        
    autosave(active_character)
    print(f"{active_character.name} successfully updated!\n\n")
