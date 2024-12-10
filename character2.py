import pickle
from culture2 import Culture2
from calling2 import Calling2
from gear2 import Weapon2, Weapons2, Armour2, Armours2, Shield2, Shields2


class Character2:
    def __init__(self, culture: Culture2, 
                 attribute_choice: int, 
                 weapon_skill_levels: dict, 
                 distinctive_features: list, 
                 name: str, age: int, 
                 calling: Calling2, 
                 favoured_skill_choices: str, 
                 starting_virtue: str, 
                 starting_reward: str):
        
        # culture
        self.culture = culture.name

        # cultural blessing
        self.blessing = culture.blessing

        # standard of living
        self.sol = culture.sol # sol = standard of living

        # attributes
        self.strength = culture.attributes[attribute_choice]["strength"]
        self.heart = culture.attributes[attribute_choice]["heart"]
        self.wits = culture.attributes[attribute_choice]["wits"]

        # attribute TNs
        self.strength_tn = 20 - self.strength
        self.heart_tn = 20 - self.heart
        self.wits_tn = 20 - self.wits

        # derived stats
        self.endurance = culture.endurance + self.strength
        self.hope = culture.hope + self.heart
        self.parry = culture.parry + self.wits

        # skills
        self.awe_level = culture.skill_levels["awe"]
        self.enhearten_level = culture.skill_levels["enhearten"]
        self.persuade_level = culture.skill_levels["persuade"]
        self.athletics_level = culture.skill_levels["athletics"]
        self.travel_level = culture.skill_levels["travel"]
        self.stealth_level = culture.skill_levels["stealth"]
        self.awareness_level = culture.skill_levels["awareness"]
        self.insight_level = culture.skill_levels["insight"]
        self.scan_level = culture.skill_levels["scan"]
        self.hunting_level = culture.skill_levels["hunting"]
        self.healing_level = culture.skill_levels["healing"]
        self.explore_level = culture.skill_levels["explore"]
        self.song_level = culture.skill_levels["song"]
        self.courtesy_level = culture.skill_levels["courtesy"]
        self.riddle_level = culture.skill_levels["riddle"]
        self.craft_level = culture.skill_levels["craft"]
        self.battle_level = culture.skill_levels["battle"]
        self.lore_level = culture.skill_levels["lore"]

        self.skill_levels = {
            "awe": self.awe_level,
            "enhearten": self.enhearten_level,
            "persuade": self.persuade_level,
            "athletics": self.athletics_level,
            "travel": self.travel_level,
            "stealth": self.stealth_level,
            "awareness": self.awareness_level,
            "insight": self.insight_level,
            "scan": self.scan_level,
            "hunting": self.hunting_level,
            "healing": self.healing_level,
            "explore": self.explore_level,
            "song": self.song_level,
            "courtesy": self.courtesy_level,
            "riddle": self.riddle_level,
            "craft": self.craft_level,
            "battle": self.battle_level,
            "lore": self.lore_level
        }

        # favoured skills
        try:
            self.favoured_skills.append(favoured_skill_choices)
        except:
            self.favoured_skills = []
            self.favoured_skills.append(favoured_skill_choices)
        
        # combat proficiencies
        self.axes_skill = weapon_skill_levels["axes"]
        self.bows_skill = weapon_skill_levels["bows"]
        self.swords_skill = weapon_skill_levels["swords"]
        self.spears_skill = weapon_skill_levels["spears"]

        self.combat_proficiencies = {
            "axes": self.axes_skill,
            "bows": self.bows_skill,
            "swords": self.swords_skill,
            "spears": self.spears_skill
        }

        # distinctive features
        self.distinctive_features = []
        for feature in distinctive_features:
            self.distinctive_features.append(feature)

        # name
        self.name = name

        # age
        self.age = age

        # calling
        self.calling = calling.name
        self.shadow_path = calling.shadow_path
        self.flaws = []

        self.patron = ""

        self.adventure_points = 0
        self.skill_points = 0
        self.fellowship_score = 0

        # gear
        self.weapons = []
        self.armour = None
        self.headgear = None
        self.shield = None

        # endurance
        self.current_endurance = self.endurance
        self.fatigue = self.load

        # hope
        self.current_hope = self.hope
        self.shadow = 0
        self.shadow_scars = 0

        # conditions
        self.is_wounded = False
        self.injury = ""

        # rewards
        self.rewards = [starting_reward]

        # virtues
        self.virtues = [starting_virtue]
    

    # conditions
    @property
    def is_miserable(self):
        if self.shadow >= self.current_hope:
            return True
        else:
            return False
        
    @property
    def is_weary(self):
        if self.current_endurance <= self.load:
            return True
        else:
            return False
        
    @property
    def load(self):
        load = 0
        for weapon in self.weapons:
            load += weapon.load

        if self.armour is not None:
            load += self.armour.load
        
        if self.headgear is not None:
            load += self.headgear.load

        if self.shield is not None:
            load += self.shield.load

        return load

    def __repr__(self):
        return (f"name: {self.name}\n"
                f"age: {self.age}\n"
                f"culture: {self.culture}\n"
                f"blessing: {self.blessing}\n"
                f"calling: {self.calling}\n"
                f"shadow path: {self.shadow_path}\n"
                f"age: {self.age}\n"
                f"patron: {self.patron}\n"
                f"standard of living: {self.sol}\n"
                f"distinctive features: {self.distinctive_features}\n"
                f"flaws: {self.flaws}\n"
                f"attributes:\n"
                    f"\tstrength:\n"
                        f"\t\tstrength rating: {self.strength}\n"
                        f"\t\tstrength TN: {self.strength_tn}\n"
                        f"\t\tendurance: {self.endurance}\n"
                    f"\theart:\n"
                        f"\t\theart rating: {self.heart}\n"
                        f"\t\theart TN: {self.heart_tn}\n"
                        f"\t\thope: {self.hope}\n"
                    f"\twits:\n"
                        f"\t\twits rating: {self.wits}\n"
                        f"\t\twits TN: {self.wits_tn}\n"
                        f"\t\tparry: {self.parry}\n"
                f"skill levels:\n"
                    f"\tawe: {self.awe_level}\t\tenhearten: {self.enhearten_level}\tpersuade: {self.persuade_level}\n"
                    f"\tathletics: {self.athletics_level}\ttravel: {self.travel_level}\tstealth: {self.stealth_level}\n"
                    f"\tawareness: {self.awareness_level}\tinsight: {self.insight_level}\tscan: {self.scan_level}\n"
                    f"\thunting: {self.hunting_level}\thealing: {self.healing_level}\texplore: {self.explore_level}\n"
                    f"\tsong: {self.song_level}\t\tcourtesy: {self.courtesy_level}\triddle: {self.riddle_level}\n"
                    f"\tcraft: {self.craft_level}\tbattle: {self.battle_level}\tlore: {self.lore_level}\n"
                f"favoured skills: {self.favoured_skills}\n"
                f"combat proficiencies:\n"
                    f"\taxes: {self.axes_skill}\n"
                    f"\tbows: {self.bows_skill}\n"
                    f"\tswords: {self.swords_skill}\n"
                    f"\tspears: {self.spears_skill}\n"
                f"rewards: {self.rewards}\n"
                f"virtues: {self.virtues}\n"
                f"war gear:\n"
                    f"\tweapons: {self.weapons}\n"
                    f"\tarmour: {self.armour}\n"
                    f"\theadgear: {self.headgear}\n"
                    f"\tshield: {self.shield}\n"
                f"adventure points: {self.adventure_points}\n"
                f"skill points: {self.skill_points}\n"
                f"fellowship score: {self.fellowship_score}\n"
                f"endurance:\n"
                    f"\tcurrent endurance {self.current_endurance}\n"
                    f"\tload: {self.load}\n"
                    f"\tfatigue: {self.fatigue}\n"
                f"hope:\n"
                    f"\tcurrent hope: {self.current_hope}\n"
                    f"\tshadow: {self.shadow}\n"
                    f"\tshadow scars: {self.shadow_scars}\n"
                f"conditions:\n"
                    f"\tis weary: {self.is_weary}\n"
                    f"\tis miserable: {self.is_miserable}\n"
                    f"\tis wounded: {self.is_wounded}\n"
                    f"\tinjury: {self.injury}\n"
    )

    # gear methods
    def add_weapon(self, weapon: Weapon2):
        self.weapons.append(weapon)

    def remove_weapon(self, weapon: str):
        for weapon in self.weapons:
            if weapon.name == weapon:
                self.weapons.remove(weapon)

    def change_armour(self, armour: Armour2):
        self.armour = armour

    def remove_armour(self):
        self.armour = None

    def change_headgear(self, headgear: Armour2):
        self.headgear = headgear

    def remove_headgear(self):
        self.headgear = None

    def change_shield(self, shield: Shield2):
        self.shield = shield

    def remove_shield(self):
        self.shield = None

    # skill methods
    def increase_skill(self, skill: str):
        self.skill_levels[skill] += 1

    def increase_combat_proficiency(self, combat_proficiency: str):
        self.combat_proficiencies[combat_proficiency] += 1

    # other characteristic methods
    def increment_age(self, increment: int=1):
        self.age += increment


def save_character(character: Character2, filename: str):
    with open(filename, "wb") as file:
        pickle.dump(character, file)


def load_character(filename: str):
    with open(filename, "rb") as file:
        character = pickle.load(file)
    return character
