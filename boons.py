"""A module containing virtues and rewards

Classes:
    Virtue: A class for virtues
    Reward: A class for rewards
"""

from dataclasses import dataclass


@dataclass
class Reward:
    """A class for rewards.
    
    Attributes:
        name (str): the name of the reward
        flavour (str): the flavour text of the reward
        effect (str): the mechanical effect of the reward
        applicibale_items (list): a list of items to which the reward may be applied
    """

    name: str
    flavour: str
    effect: str
    applicibale_items: list

    def __init__(self, name = None, flavour = None, effect = None, applicibale_items = None):
        self.name = name
        self.flavour = flavour
        self.effect = effect
        self.applicibale_items = applicibale_items

    def __repr__(self):
        return f"{self.name} - {self.effect}"


@dataclass
class Virtue:
    """A class for virtues.
    
    Attributes:
        name (str): the name of the virtue
        flavour (str): the flavour text of the virtue
        effect (str): the mechanical effect of the virtue
    """
    name: str
    flavour: str
    effect: str

    def __init__(self, name = None, flavour = None, effect = None):
        self.name = name
        self.flavour = flavour
        self.effect = effect

    def __repr__(self):
        return f"{self.name} - {self.effect}"
