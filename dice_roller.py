import random
import os

from character import Character, load_character


def clear_console(active_character):
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    print("One Ring RPG Character Manager\n"
          "Enter \'help\' at any time for a list of commands or \'exit\' to quit\n")


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
            print("1")
            if die == 6:
                quality_of_success += 1
            total += die
            dice_to_roll -= 1
        if quality_of_success > 2:
            quality_of_success = 2
        return total, feat_die, quality_of_success
    

def rollable_items(active_character: Character):
    title()
    print("\nItems to roll:\n")
    for skill in active_character.skill_levels:
        print(skill)
    for combat_proficiency in active_character.combat_proficiencies:
        print(combat_proficiency)
    print("armour")



def select_character_to_load(character_name: str):
    if character_name is None:
        print("Enter the name of the character to load: ")
        filename = input("> ").lower()
    else:
        filename = character_name

    while True:
        try:
            active_character = load_character(f"{filename}.pickle")
            break
        except FileNotFoundError:
            print("No character with that name was found. Please enter a different name")
            filename = input("> ").lower()

    clear_console(active_character)
    print(f"{active_character.name} successfully loaded!\n")
    return active_character


def roll_skill(active_character: Character, attribute: str):
    clear_console(active_character)
    if attribute is None:
        print("Enter the attribute you would like to see:")
        attribute = input("> ")
    match attribute:
        case "help":
            clear_console
            rollable_items()
        case _:
            clear_console(active_character)
            if attribute == "armour":
                print(f"{roll(active_character.armour.protection, True, False)}\n")
            if attribute in active_character.combat_proficiencies:
                print(f"{roll(active_character.combat_proficiencies[attribute], True, False)}\n")
            try:
                print(f"{roll(getattr(active_character, attribute), True, False)}\n")
            except AttributeError:
                print("Attribute not found\n")


if __name__ == "__main__": 
    active_character = select_character_to_load("Lif") 
    rollable_items(active_character)
    roll_skill(active_character, "bows")
    