from utils import MetaEnum
from dataclasses import dataclass


@dataclass
class Blessing2:
    name: str
    flavour: str
    effect: str
    quote: str

    def __repr__(self):
        return f"{self.name} - {self.effect}"


class Blessings2(metaclass=MetaEnum):
    STOUT_HEARTED = Blessing2(
        name="Stout Hearted",
        flavour="Stories tell that the Bardings lived under the shadow of a great Dragon for decades.",
        effect="Your VALOUR rolls are Favoured",
        quote="To the lineage of Gondor he added the fearless spirit of the Northmen..."
    )
    REDOUBTABLE = Blessing2(
        name="Redoubtable",
        flavour="Dwarves make light of burdens, especially when it comes to wearing armour.",
        effect="You halve the Load rating of any armour you’re wearing (rounding fractions up), including helms (but not shields).",
        quote="Gimli the dwarf alone wore openly a short shirt of steel-rings, for dwarves make light of burdens..."
    )
    ELVEN_SKILL = Blessing2(
        name="Elven Skill",
        flavour="By virtue of their birthright, Elves are capable of reaching levels of finesse unattainable by mortals",
        effect="Whenever you are making a Skill roll, you can spend 1 Hope to achieve a Magical success.",
        quote="“Keen are the eyes of the Elves,” he said. “Nay! The riders are little more than five leagues distant,” said Legolas."
    )
    HOBBIT_SENSE = Blessing2(
        name="Hobbit Sense",
        flavour=("Hobbits have learned their place in the world a long time ago, and they display a robust capacity for insight that many folks mistake for lack of "
                 "courage. No visions or wild fantasies can tempt them, as they do not seek power or control over others."),
        effect="Your WISDOM rolls are Favoured.",
        quote="… they have a fund of wisdom and wise sayings that men have mostly never heard or have forgotten long ago"
    )
    BREE_BLOOD = Blessing2(
        name="Bree Blood",
        flavour=("Due to the position of their homeland, the Men of Bree enjoy better relationships with Hobbits, Dwarves, "
                "Elves, and other inhabitants of the world about them than is considered usual."),
        effect="Each Man of Bree in the Company increases the Fellowship Rating by 1 point.",
        quote="The Men of Bree were brown-haired, broad, and rather short, cheerful and independent: they belonged to nobody but themselves..."
    )
    KINGS_OF_MEN = Blessing2(
        name="Kings of Men",
        flavour=("Some say that the lordship of the folk of Arnor is a thing of the past. Yet, the Rangers of the North have "
                 "inherited the sinews of those Men who wrested the Ring from the burning hand of Sauron."),
        effect="Add 1 point to one Attribute of your choice.",
        quote="They were fair of face and tall, and the span of their lives was thrice that of the Men of Middle-earth."
    )

    @classmethod
    def by_name(cls, name):
        for blessing in Blessings2:
            if type(blessing) is Blessing2:
                if blessing.name == name:
                    return blessing
    
    @classmethod
    def names(cls):
        names = []
        for blessing in Blessings2:
            if type(blessing) is Blessing2:
                names.append(blessing.name)
        return names