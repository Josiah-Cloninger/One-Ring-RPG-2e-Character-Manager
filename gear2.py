from utils import MetaEnum
from dataclasses import dataclass


@dataclass
class Weapon2:
    name: str
    damage: int
    injury: int
    load: int
    skill: str
    notes: str = ""
    is_versatile: bool=False
    is_two_handed: bool=False
    is_ranged: bool=False
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, damage: {self.damage}, injury: {self.injury}, load:{self.load}"


class Weapons2(metaclass=MetaEnum):
    UNARMED = Weapon2("Unarmed", damage=1, injury=0, load=0, skill="brawling", notes="Includes throwing stones. Cannot cause a Piercing Blow")
    DAGGER = Weapon2("Dagger", damage=2, injury=12, load=0, skill="brawling")
    CUDGEL = Weapon2("Cudgel", damage=3, injury=12, load=0, skill="brawling")
    SHORT_SWORD = Weapon2("Short Sword", damage=3, injury=16, load=1, skill="swords")
    SWORD = Weapon2("Sword", damage=4, injury=16, load=2, skill="swords")
    LONG_SWORD = Weapon2("Long Sword", damage=5, injury=16, load=3, skill="swords", is_versatile=True)
    SHORT_SPEAR = Weapon2("Short Spear", damage=3, injury=14, load=2, skill="spear", is_ranged=True)
    SPEAR = Weapon2("Spear", damage=4, injury=14, load=3, skill="spear",is_versatile=True, is_ranged=True)
    GREAT_SPEAR = Weapon2("Great Spear", damage=5, injury=16, load=4, skill="spear")
    AXE = Weapon2("Axe", damage=5, injury=18, load=2, skill="axes")
    CLUB = Weapon2("Club", damage=4, injury=14, load=1, skill="axes")
    LONG_HAFTED_AXE = Weapon2("Long-hafted Axe", damage=6, injury=18, load=3, skill="axes", is_versatile=True)
    GREAT_AXE = Weapon2("Great Axe", damage=7, injury=20, load=4, skill="axes", is_two_handed=True)
    MATTOCK = Weapon2("Mattock", damage=6, injury=18, load=3, skill="axes", is_two_handed=True)
    BOW = Weapon2("Bow", damage=3, injury=14, load=2, skill="bows", is_ranged=True)
    GREAT_BOW = Weapon2("Great Bow", damage=4, injury=16, load=4, skill="bows", is_ranged=True)

    @classmethod
    def by_name(cls, name):
        for weapon in Weapons2:
            if type(weapon) is Weapon2:
                if weapon.name == name:
                    return weapon
    
    @classmethod
    def names(cls):
        names = []
        for weapon in Weapons2:
            if type(weapon) is Weapon2:
                names.append(weapon.name)
        return names


@dataclass
class Armour2:
    name: str
    protection: int
    load: int
    type: str
    sol_requirement: str
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, protection: {self.protection}, load: {self.load}"


class Armours2(metaclass=MetaEnum):
    LEATHER_SHIRT = Armour2("Leather shirt", protection=1, load=3, type="Leather armour", sol_requirement="none")
    LEATHER_CORSLET = Armour2("Leather corslet", protection=2, load=6, type="light", sol_requirement="none")
    MAIL_SHIRT = Armour2("Mail shirt", protection=3, load=9, type="light", sol_requirement="Common")
    COAT_OF_MAIL = Armour2("Coat of mail", protection=4, load=12, type="light", sol_requirement="Prosperous")

    @classmethod
    def by_name(cls, name):
        for armour in Armours2:
            if type(armour) is Armour2:
                if armour.name == name:
                    return armour
    
    @classmethod
    def names(cls):
        names = []
        for armour in Armours2:
            if type(armour) is Armour2:
                names.append(armour.name)
        return names


@dataclass
class Headgear2:
    name: str
    protection: int
    load: int
    type: str
    sol_requirement: str
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, protection: {self.protection}, load: {self.load}"


class Headgears2(metaclass=MetaEnum):
    HELM = Headgear2("Helm", protection=1, load=4, type="Headgear", sol_requirement="none")

    @classmethod
    def by_name(cls, name):
        for headgear in Headgears2:
            if type(headgear) is Headgear2:
                if headgear.name == name:
                    return headgear
    
    @classmethod
    def names(cls):
        names = []
        for headgear in Headgears2:
            if type(headgear) is Headgear2:
                names.append(headgear.name)
        return names


@dataclass
class Shield2:
    name: str
    parry_mod: int
    load: int
    sol_requirement: str
    notes: str = ""

    def __repr__(self):
        return f"{self.name}, parry modifier: {self.parry_mod}, load: {self.load}"


class Shields2(metaclass=MetaEnum):
    BUCKLER = Shield2("Buckler", parry_mod=1, load=2, sol_requirement="none")
    SHIELD = Shield2("Shield", parry_mod=2, load=4, sol_requirement="Common")
    GREAT_SHIELD = Shield2("Great Shield", parry_mod=3, load=6, sol_requirement="Prosperous")

    @classmethod
    def by_name(cls, name):
        for shield in Shields2:
            if type(shield) is Shield2:
                if shield.name == name:
                    return shield
    
    @classmethod
    def names(cls):
        names = []
        for shield in Shields2:
            if type(shield) is Shield2:
                names.append(shield.name)
        return names
