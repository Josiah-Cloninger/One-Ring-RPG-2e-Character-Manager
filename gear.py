"""A module containing gear

Classes:
    Weapon: A class representing a weapon.
    Weapons: An enumeration of weapons.
    Armour: A class representing armour.
    Armours: An enumeration of armours.
    Headgear: A class representing headgear.
    Headgears: An enumeration of headgears.
    Shield: A class representing a shield.
    Shields: An enumeration of shields.
"""

from dataclasses import dataclass
from utils import MetaEnum


@dataclass
class Weapon:
    """A class representing a weapon.
    
    Attributes:
        name (str): The name of the weapon.
        damage (int): How much endurance loss the weapon inflicts.
        injury (int): The TN for protection tests made in response to piercing blows inflicted by the weapon.
        load (int): The load of the weapon.
        skill (str): The combat proficiency associated with the weapon.
        notes (str): Any additional notes about the weapon.
        is_versatile (bool): Whether the weapon can be used either 1 or 2 handed.
        is_two_handed (bool): Whether the weapon is two handed.
        is_ranged (bool): Whether the weapon is ranged.
    """

    name: str
    damage: int
    injury: int
    load: int
    skill: str
    is_versatile: bool=False
    is_two_handed: bool=False
    is_ranged: bool=False
    notes: str = ""

    def __repr__(self):
        return f"name: {self.name}, damage: {self.damage}, injury: {self.injury}, load: {self.load}, notes: {self.notes}\n"


class Weapons(metaclass=MetaEnum):
    """An enumeration of weapons.
    
    Methods:
        by_name(name): Return the weapon with the given name.
        names(): Return the names of all weapons.
    """

    UNARMED = Weapon("Unarmed", damage=1, injury=0, load=0, skill="brawling", notes="Includes throwing stones. Cannot cause a Piercing Blow")
    DAGGER = Weapon("Dagger", damage=2, injury=12, load=0, skill="brawling")
    CUDGEL = Weapon("Cudgel", damage=3, injury=12, load=0, skill="brawling")
    SHORT_SWORD = Weapon("Short Sword", damage=3, injury=16, load=1, skill="swords")
    SWORD = Weapon("Sword", damage=4, injury=16, load=2, skill="swords")
    LONG_SWORD = Weapon("Long Sword", damage=5, injury=16, load=3, skill="swords", is_versatile=True)
    SHORT_SPEAR = Weapon("Short Spear", damage=3, injury=14, load=2, skill="spear", is_ranged=True)
    SPEAR = Weapon("Spear", damage=4, injury=14, load=3, skill="spear",is_versatile=True, is_ranged=True)
    GREAT_SPEAR = Weapon("Great Spear", damage=5, injury=16, load=4, skill="spear")
    AXE = Weapon("Axe", damage=5, injury=18, load=2, skill="axes")
    CLUB = Weapon("Club", damage=4, injury=14, load=1, skill="axes")
    LONG_HAFTED_AXE = Weapon("Long-hafted Axe", damage=6, injury=18, load=3, skill="axes", is_versatile=True)
    GREAT_AXE = Weapon("Great Axe", damage=7, injury=20, load=4, skill="axes", is_two_handed=True)
    MATTOCK = Weapon("Mattock", damage=6, injury=18, load=3, skill="axes", is_two_handed=True)
    BOW = Weapon("Bow", damage=3, injury=14, load=2, skill="bows", is_ranged=True)
    GREAT_BOW = Weapon("Great Bow", damage=4, injury=16, load=4, skill="bows", is_ranged=True)

    @classmethod
    def by_name(cls, name):
        """Return the weapon with the given name.
        
        Args:
            name (str): The name of the weapon.
        
        Returns:
            Weapon: The weapon with the given name.
        """

        for weapon in Weapons:
            if isinstance(weapon, Weapon):
                if weapon.name == name:
                    return weapon

    @classmethod
    def names(cls):
        """Return the names of all weapons.
        
        Returns:
            list: A list of the names of all weapons.
        """
        names = []
        for weapon in Weapons:
            if isinstance(weapon, Weapon):
                names.append(weapon.name)
        return names


@dataclass
class Armour:
    """A class representing armour.
    
    Attributes:
        name (str): The name of the armour.
        protection (int): The number of additional success dice the wearer of the armour rolls when making a protection test.
        load (int): The load of the armour.
        type (str): What the armour is made of.
        sol_requirement (str): The standard of living requirement for the armour.
        notes (str): Any additional notes about the armour.
    """

    name: str
    protection: int
    load: int
    type: str
    sol_requirement: str
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, protection: {self.protection}, load: {self.load}"


class Armours(metaclass=MetaEnum):
    """An enumeration of armours.
    
    Methods:
        by_name(name): Return the armour with the given name.
        names(): Return the names of all armours.
    """
    LEATHER_SHIRT = Armour("Leather shirt", protection=1, load=3, type="Leather armour", sol_requirement="none")
    LEATHER_CORSLET = Armour("Leather corslet", protection=2, load=6, type="light", sol_requirement="none")
    MAIL_SHIRT = Armour("Mail shirt", protection=3, load=9, type="light", sol_requirement="Common")
    COAT_OF_MAIL = Armour("Coat of mail", protection=4, load=12, type="light", sol_requirement="Prosperous")

    @classmethod
    def by_name(cls, name):
        """Return the armour with the given name.
        
        Args:
            name (str): The name of the armour.
        
        Returns:
            Armour: The armour with the given name.
        """
        for armour in Armours:
            if isinstance(armour, Armour):
                if armour.name == name:
                    return armour

    @classmethod
    def names(cls):
        """Return the names of all armours.
        
        Returns:
            list: A list of the names of all armours.
        """
        names = []
        for armour in Armours:
            if isinstance(armour, Armour):
                names.append(armour.name)
        return names


@dataclass
class Headgear:
    """A class representing headgear.
    
    Attributes:
        name (str): The name of the headgear.
        protection (int): The number of additional success dice the wearer of the headgear rolls when making a protection test.
        load (int): The load of the headgear.
        type (str): What the headgear is made of.
        sol_requirement (str): The standard of living requirement for the headgear.
        notes (str): Any additional notes about the headgear.
    """

    name: str
    protection: int
    load: int
    type: str
    sol_requirement: str
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, protection: {self.protection}, load: {self.load}"


class Headgears(metaclass=MetaEnum):
    """An enumeration of headgear.
    
    Methods:
        by_name(name): Return the headgear with the given name.
        names(): Return the names of all headgear.
    """

    HELM = Headgear("Helm", protection=1, load=4, type="Headgear", sol_requirement="none")

    @classmethod
    def by_name(cls, name):
        """Return the headgear with the given name.
        
        Args:
            name (str): The name of the headgear.
        
        Returns:
            Headgear: The headgear with the given name.
        """
        for headgear in Headgears:
            if isinstance(headgear, Headgear):
                if headgear.name == name:
                    return headgear

    @classmethod
    def names(cls):
        """Return the names of all headgear.
        
        Returns:
            list: A list of the names of all headgear.
        """
        names = []
        for headgear in Headgears:
            if isinstance(headgear, Headgear):
                names.append(headgear.name)
        return names


@dataclass
class Shield:
    """A class representing shields.
    
    Attributes:
        name (str): The name of the shield.
        parry_mod (int): The bonus to parry the weilder recieves while this shield is equipped.
        load (int): The load of the shield.
        sol_requirement (str): The standard of living requirement for the shield.
        notes (str): Any additional notes about the shield.    
    """

    name: str
    parry_mod: int
    load: int
    sol_requirement: str
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, parry modifier: {self.parry_mod}, load: {self.load}"


class Shields(metaclass=MetaEnum):
    """An enumeration of shields.
    
    Methods:
        by_name(name): Return the shield with the given name.
        names(): Return the names of all shields.
    """

    BUCKLER = Shield("Buckler", parry_mod=1, load=2, sol_requirement="none")
    SHIELD = Shield("Shield", parry_mod=2, load=4, sol_requirement="Common")
    GREAT_SHIELD = Shield("Great Shield", parry_mod=3, load=6, sol_requirement="Prosperous")

    @classmethod
    def by_name(cls, name):
        """Return the shield with the given name.

        Args:
            name (str): The name of the shield to return.

        Returns:
            Shield: The shield with the given name, or None if no shield has that name.
        """

        for shield in Shields:
            if isinstance(shield, Shield):
                if shield.name == name:
                    return shield

    @classmethod
    def names(cls):
        """Return the names of all shields.
        
        Returns:
            list: A list of the names of all shields.
        """

        names = []
        for shield in Shields:
            if isinstance(shield, Shield):
                names.append(shield.name)
        return names
