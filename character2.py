import pickle
from culture2 import Culture2
from calling2 import Calling2
from gear2 import Weapon2, Weapons2, Armour2, Armours2, Shield2, Shields2
from standard_of_living import Standard_Of_Living, Standards_Of_Living


NOT_ENOUGH_TREASURE = Exception("Not enough treasure points")
NOT_ENOUGH_SKILL_POINTS = Exception("Not enough skill points.")
NOT_ENOUGH_ADVENTURE_POINTS = Exception("Not enough adventure points.")


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
        self.standard_of_living = culture.sol # sol = standard of living
        self.treasure = self.standard_of_living.treasure_rating

        # attributes
        self.strength_score = attribute_choice["strength"]
        self.heart_score = attribute_choice["heart"]
        self.wits_score = attribute_choice["wits"]

        # attribute TNs
        self.strength_tn = 20 - self.strength_score
        self.heart_tn = 20 - self.heart_score
        self.wits_tn = 20 - self.wits_score

        # derived stats
        self.max_endurance = culture.endurance + self.strength_score
        self.max_hope = culture.hope + self.heart_score
        self.parry = culture.parry + self.wits_score

        # skills
        self.awe = culture.skill_levels["awe"]
        self.enhearten = culture.skill_levels["enhearten"]
        self.persuade = culture.skill_levels["persuade"]
        self.athletics = culture.skill_levels["athletics"]
        self.travel = culture.skill_levels["travel"]
        self.stealth = culture.skill_levels["stealth"]
        self.awareness = culture.skill_levels["awareness"]
        self.insight = culture.skill_levels["insight"]
        self.scan = culture.skill_levels["scan"]
        self.hunting = culture.skill_levels["hunting"]
        self.healing = culture.skill_levels["healing"]
        self.explore = culture.skill_levels["explore"]
        self.song = culture.skill_levels["song"]
        self.courtesy = culture.skill_levels["courtesy"]
        self.riddle = culture.skill_levels["riddle"]
        self.craft = culture.skill_levels["craft"]
        self.battle = culture.skill_levels["battle"]
        self.lore = culture.skill_levels["lore"]

        self.skill_levels = {
            "awe": self.awe,
            "enhearten": self.enhearten,
            "persuade": self.persuade,
            "athletics": self.athletics,
            "travel": self.travel,
            "stealth": self.stealth,
            "awareness": self.awareness,
            "insight": self.insight,
            "scan": self.scan,
            "hunting": self.hunting,
            "healing": self.healing,
            "explore": self.explore,
            "song": self.song,
            "courtesy": self.courtesy,
            "riddle": self.riddle,
            "craft": self.craft,
            "battle": self.battle,
            "lore": self.lore
        }

        # favoured skills
        try:
            self.favoured_skills.append(favoured_skill_choices)
        except:
            self.favoured_skills = []
            self.favoured_skills.append(favoured_skill_choices)
        
        # combat proficiencies
        self.axes_skill = weapon_skill_levels.get("axes")
        self.bows_skill = weapon_skill_levels.get("bows")
        self.swords_skill = weapon_skill_levels.get("swords")
        self.spears_skill = weapon_skill_levels.get("spears")

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
        self.current_endurance = self.max_endurance
        self.fatigue = 0

        # hope
        self.current_hope = self.max_hope
        self.shadow_points = 0
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
        if self.shadow_points + self.shadow_scars >= self.current_hope:
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


    @property
    def standard_of_living(self):
        match self.treasure:
            case range(0, 30):
                return Standards_Of_Living.FRUGAL
            case range(30, 90):
                return Standards_Of_Living.COMMON
            case range(90, 180):
                return Standards_Of_Living.PROSPEROUS
            case range(180, 300):
                return Standards_Of_Living.RICH
            case range(300, 1000):
                return Standards_Of_Living.VERY_RICH


    def add_treasure(self, value: int):
        if self.treasure > -value:
            self.treasure += value
        else:
            raise NOT_ENOUGH_TREASURE


    def upgrade_skill(self, skill: str):
        if self.skill_points >= upgrade_table(self.skill_levels[skill].level + 1):
            self.skill_levels[skill] += 1
            self.skill_points -= upgrade_table(self.skill_levels[skill])
        else:
            raise NOT_ENOUGH_SKILL_POINTS


    def upgrade_combat_proficiency(self, combat_proficiency: str):
        if self.adventure_points >= upgrade_table(self.combat_proficiencies[combat_proficiency].level + 1):
            self.combat_proficiencies[combat_proficiency] += 1
            self.adventure_points -= upgrade_table(self.combat_proficiencies[combat_proficiency].level)
        else:
            raise NOT_ENOUGH_ADVENTURE_POINTS


    def increment_age(self, increment: int=1):
        self.age += increment


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


    def __repr__(self):
        return (f"name: {self.name}\n"
                f"age: {self.age}\n"
                f"culture: {self.culture}\n"
                f"blessing: {self.blessing}\n"
                f"calling: {self.calling}\n"
                f"shadow path: {self.shadow_path}\n"
                f"patron: {self.patron}\n"
                f"standard of living: {self.standard_of_living}\n"
                f"treasure: {self.treasure}\n"
                f"distinctive features: {self.distinctive_features}\n"
                f"flaws: {self.flaws}\n"
                f"attributes:\n"
                    f"\tstrength:\n"
                        f"\t\tstrength rating: {self.strength_score}\n"
                        f"\t\tstrength TN: {self.strength_tn}\n"
                        f"\t\tendurance: {self.max_endurance}\n"
                    f"\theart:\n"
                        f"\t\theart rating: {self.heart_score}\n"
                        f"\t\theart TN: {self.heart_tn}\n"
                        f"\t\thope: {self.max_hope}\n"
                    f"\twits:\n"
                        f"\t\twits rating: {self.wits_score}\n"
                        f"\t\twits TN: {self.wits_tn}\n"
                        f"\t\tparry: {self.parry}\n"
                f"skill levels:\n"
                    f"\tawe: {self.awe}\t\tenhearten: {self.enhearten}\tpersuade: {self.persuade}\n"
                    f"\tathletics: {self.athletics}\ttravel: {self.travel}\tstealth: {self.stealth}\n"
                    f"\tawareness: {self.awareness}\tinsight: {self.insight}\tscan: {self.scan}\n"
                    f"\thunting: {self.hunting}\thealing: {self.healing}\texplore: {self.explore}\n"
                    f"\tsong: {self.song}\t\tcourtesy: {self.courtesy}\triddle: {self.riddle}\n"
                    f"\tcraft: {self.craft}\tbattle: {self.battle}\tlore: {self.lore}\n"
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
                    f"\tshadow points: {self.shadow_points}\n"
                    f"\tshadow scars: {self.shadow_scars}\n"
                f"conditions:\n"
                    f"\tis weary: {self.is_weary}\n"
                    f"\tis miserable: {self.is_miserable}\n"
                    f"\tis wounded: {self.is_wounded}\n"
                    f"\tinjury: {self.injury}\n"
    )


def save_character(character: Character2, filename: str):
    with open(filename, "wb") as file:
        pickle.dump(character, file)


def load_character(filename: str):
    with open(filename, "rb") as file:
        character = pickle.load(file)
    return character


def upgrade_table(input: int):
    match input:
        case 1:
            return 4
        case 2:
            return 8
        case 3:
            return 12
        case 4:
            return 20
        case 5:
            return 26
        case 6:
            return 30

