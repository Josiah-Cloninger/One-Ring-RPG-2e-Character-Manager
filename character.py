"""A module containing the Character class.

Classes:
    Character: A class for a character

Exceptions:
    TreasureError: An exception raised when not enough treasure points are available
    SkillPointError: An exception raised when not enough skill points are available
    AdventurePointError: An exception raised when not enough adventure points are available

Functions:
    load_character(filename: str): Loads a character from a file.
    upgrade_table(level: int): Converts form level to points.
"""

import pickle
from culture import Culture
from calling import Calling
from standard_of_living import StandardsOfLiving


TreasureError = Exception("Not enough treasure points")
SkillPointError = Exception("Not enough skill points.")
AdventurePointError = Exception("Not enough adventure points.")


class Character:
    """A class for a character.
    
    Attributes:
        culture (Culture): The heroic culture that the character belongs to.
        blessing (Blessing): The cultural blessing the character recieved from their culture.
        treasure (int): The treasure rating of the character.
        strength_score (int): The strength score of the character.
        heart_score (int): The heart score of the character.
        wits_score (int): The wits score of the character.
        strength_tn (int): The TN for the character's Strength Skills.
        heart_tn (int): The TN for the character's Heart Skills.
        wits_tn (int): The TN for the character's Wits Skills.
        max_endurance (int): The maximum endurance the character can have.
        max_hope (int): The maximum hope the character can have.
        parry (int): The parry rating of the character.
        awe (int): The awe level of the character.
        enhearten (int): The enhearten level of the character.
        persuade (int): The persuade level of the character.
        athletics (int): The athletics level of the character.
        travel (int): The travel level of the character.
        stealth (int): The stealth level of the character.
        awareness (int): The awareness level of the character.
        insight (int): The insight level of the character.
        scan (int): The scan level of the character.
        hunting (int): The hunting level of the character.
        healing (int): The healing level of the character.
        explore (int): The explore level of the character.
        song (int): The song level of the character.
        courtesy (int): The courtesy level of the character.
        riddle (int): The riddle level of the character.
        craft (int): The craft level of the character.
        battle (int): The battle level of the character.
        lore (int): The lore level of the character.
        favoured_skills (list[str]): The favoured skills of the character.
        combat_proficiencies (dict[str, int]): The levels of the combat proficiencies of the character.
        distinctive_features (list[str]): The distinctive features of the character.
        name (str): The name of the character.
        age (int): The age of the character.
        calling (Calling): The calling of the character.
        shadow_path (Calling): The shadow path of the character.
        flaws (list[str]): The flaws of the character.
        patron (str): The patron of the character.
        adventure_points (int): The adventure points of the character.
        skill_points (int): The skill points of the character.
        fellowship_score (int): The fellowship score of the character.
        weapons (list[Weapon]): The weapons the character has.
        armour (Armour): The armour the character has.
        headgear (Headgear): The headgear the character has.
        shield (Shield): The shield the character has.
        current_endurance (int): The current endurance of the character.
        fatigue (int): The fatigue of the character.
        current_hope (int): The current hope of the character.
        shadow_points (int): The shadow points of the character.
        shadow_scars (int): The shadow scars of the character.
        is_wounded (bool): Whether the character is wounded or not.
        injury (int): How many more days the character will be wounded.
        valour (int): The valour rating of the character
        rewards (list[Reward]): The rewards the character has.
        wisdom (int): The wisdom rating of the character.
        virtues (list[Virtue]): The virtues the character has.
        traveling_gear (list[str]): The traveling gear the character has.

    Properties:
        is_weary (bool): Whether the character is weary or not.
        is_miserable (bool): Whether the character is miserable or not.
        standard_of_living (Standard_Of_Living): The standard at which the character lives.
        axes_skill (int): The axes skill of the character.
        bows_skill (int): The bows skill of the character.
        spears_skill (int): The spears skill of the character.
        swords_skill (int): The swords skill of the character.
        shadow (int): The shadow value of a character (the shadow points plus the shadow scars).

    Methods: 
        virtues_by_name(virtue_name: str): Returns the character's virtue with the given name.
        rewards_by_name(reward_name: str): Returns the character's reward with the given name.
        weapons_by_name(weapon_name: str): Returns the character's weapon with the given name.
        save_character: Saves the character to a pickle file.
    """

    def __init__(self, culture: Culture = None,
                 attribute_choice: int = None,
                 weapon_skill_levels: dict = None,
                 distinctive_features: list = None,
                 name: str = None, age: int = None,
                 calling: Calling = None,
                 favoured_skills: list[str] = None,
                 starting_virtue: str = None,
                 starting_reward: str = None):

        # culture
        self.culture = culture.name

        # cultural blessing
        self.blessing = culture.blessing

        # standard of living
        self.treasure = culture.sol.treasure_rating

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
        self.favoured_skills = favoured_skills

        self.combat_proficiencies = {
            "axes": weapon_skill_levels.get("axes"),
            "bows": weapon_skill_levels.get("bows"),
            "spears": weapon_skill_levels.get("spears"),
            "swords": weapon_skill_levels.get("swords")
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
        self.injury = 0

        # rewards
        self.valour = 1
        self.rewards = [starting_reward]

        # virtues
        self.wisdom = 1
        self.virtues = [starting_virtue]

        self.traveling_gear = [str]


    @property
    def is_miserable(self):
        """Return True if the character's current hope is less than or equal to their shadow scars + shadow points."""
        if self.shadow_points + self.shadow_scars >= self.current_hope:
            return True
        return False

    @property
    def is_weary(self):
        """Return True if the character's current endurance is less than or equal to their load."""
        if self.current_endurance <= self.load:
            return True
        return False

    @property
    def load(self):
        """Calculate the character's load by adding the load of all their war gear."""

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
        """Return the character's standard of living based on their treasure."""
        match self.treasure:
            case range(0, 30):
                return StandardsOfLiving.FRUGAL
            case range(30, 90):
                return StandardsOfLiving.COMMON
            case range(90, 180):
                return StandardsOfLiving.PROSPEROUS
            case range(180, 300):
                return StandardsOfLiving.RICH
            case range(300, 1000):
                return StandardsOfLiving.VERY_RICH

    @property
    def axes_skill(self):
        """Return the character's axes skill."""
        return self.combat_proficiencies["axes"]

    @property
    def bows_skill(self):
        """Return the character's bows skill."""
        return self.combat_proficiencies["bows"]

    @property
    def spears_skill(self):
        """Return the character's spears skill."""
        return self.combat_proficiencies["spears"]

    @property
    def swords_skill(self):
        """Return the character's swords skill."""
        return self.combat_proficiencies["swords"]

    @property
    def shadow(self):
        """Return the character's total shadow rating."""
        return self.shadow_points + self.shadow_scars


    def virtues_by_name(self, virtue_name: str):
        """Return the virtue this character has with a given name.
        
        Args:
            virtue_name (str): The name of the virtue to return.
        
        Return:
            Virtue: The virtue with the given name
        """

        for virtue in self.virtues:
            if virtue.name == virtue_name:
                return virtue
        return None

    def rewards_by_name(self, reward_name: str):
        """Return the reward this character has with a given name.
        
        Args:
            reward_name (str): The name of the reward to return.
        
        Return:
            Reward: The reward with the given name
        """

        for reward in self.rewards:
            if reward.name == reward_name:
                return reward
        return None

    def weapons_by_name(self, weapon_name: str):
        """Return the weapon this character has with a given name.
        
        Args:
            weapon_name (str): The name of the weapon to return.
        
        Return:
            Weapon: The weapon with the given name"""
        for weapon in self.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def save_character(self):
        """Save the character as a .pickle file named '{character name}_hardsave.pickle'."""
        with open(f"{self.name}_hardsave.pickle", "wb") as file:
            pickle.dump(self, file)

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

def load_character(character_name: str):
    """Load a character from a pickle file.
    
    Tries to load the character from the {character name}_autosave.pickle file.
    If that file is not found, loads from the {character name}_hardsave.pickle file.

    Args:
        character_name (str): The name of the character to load.

    Returns:
        Character: The loaded character.
    """

    try:
        with open(f"{character_name}_autosave.pickle", "rb") as file:
            character = pickle.load(file)
    except FileNotFoundError:
        with open(f"{character_name}_hardsave.pickle", "rb") as file:
            character = pickle.load(file)
    return character

def upgrade_table(level: int):
    """Convert attribute level to points required to upgrade.
    
    Args:
        level (int): The level of the attribute to upgrade.

    Returns:
        int: The number of points (adventure points or skill points) required to upgrade the attribute.
    """
    match level:
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
