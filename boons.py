from dataclasses import dataclass


@dataclass
class Reward:
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
    name: str
    flavour: str
    effect: str

    def __init__(self, name = None, flavour = None, effect = None):
        self.name = name
        self.flavour = flavour
        self.effect = effect

    def __repr__(self):
        return f"{self.name} - {self.effect}"
