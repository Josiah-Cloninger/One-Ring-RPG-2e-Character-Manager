import os


import character_creation


from character2 import Character2, load_character, save_character


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


acceptable_commands = {
    "help": "Prints a list of commands",
    "exit": "Exits the program",
    "create character": "Creates a new character",
    "save": "Saves a character",
    "load": "Loads a character",
}


while True:
    clear_console()
    print("One Ring RPG Character Manager\n\n")
    print("Enter a command or \"help\" for a list of commands: ")
    command = input()
    match command:
        case "help":
            for command, description in acceptable_commands.items():
                print(f"{command}: {description}")
            
        case "exit":
            print("Goodbye!")
            break
        case "create character":
            active_character = character_creation.main()
            print(active_character)
            
        case "save":
            save_character(active_character, f"{active_character.name}.pickle")
            print(f"Character saved to {active_character.name}.pickle")
            
        case "load":
            print("Enter the name of the character to load: ")
            filename = input("> ")
            filename = "Dervorin"
            active_character = load_character(f"{filename}.pickle")
            print(active_character)
            
        
        # information
        case "culture":
            print(f"Culture: {active_character.culture}")
            
        case "age":
            print(f"Age: {active_character.age}")
            
        case "distinctive features":
            print(f"Distinctive Features: {active_character.distinctive_features}")
            
        case "blessing":
            print(f"Blessing: {active_character.blessing}")
            
        case "standard of living":
            print(f"Standard of Living {active_character.sol}")
            
        case "treasure":
            print(f"Treasure: {active_character.treasure}")
            
        case "calling":
            print(f"Calling: {active_character.calling}")
            
        case "shadow path":
            print(f"Shadow Path: {active_character.shadow_path}")
            
        case "flaws":
            print("Flaws: {active_character.flaws}")
            

        # Attributes
        case "strength":
            print(f"Strength Rating: {active_character.strength}")
            print(f"Strength TN: {active_character.strength_tn}")
            print(f"Max Endurance: {active_character.endurance}")
            
        case "heart":
            print(f"Heart Rating: {active_character.heart}")
            print(f"Heart TN: {active_character.heart_tn}")
            print(f"Max Hope: {active_character.hope}")
            
        case "wits":
            print(f"Wits Rating: {active_character.wits}")
            print(f"Wits TN: {active_character.wits_tn}")
            print(f"Parry: {active_character.parry}")
            
        case "endurance":
            print(f"Current Endurance: {active_character.current_endurance}")
            
        case "hope":
            print(f"Current Hope: {active_character.current_hope}")
            
        case "parry":
            print(f"Parry: {active_character.parry}")
            
        
        # Skills
        case "skill levels":
            for skill in active_character.skill_levels:
                print(f"{skill}: {active_character.skill_levels[skill]}")
                
        case "favoured skills":
            print(f"Favoured Skills: {active_character.favoured_skills}")
            

        # Combat Proficiencies
        case "combat proficiencies":
            print(f"Combat Proficiencies: {active_character.combat_proficiencies}")
            

        case _:
            print("Invalid command")
            
    input("Press enter to continue")
