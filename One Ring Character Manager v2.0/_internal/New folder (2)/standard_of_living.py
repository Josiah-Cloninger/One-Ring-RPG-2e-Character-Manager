from utils import MetaEnum
from dataclasses import dataclass


@dataclass
class Standard_Of_Living():
    level: int
    name: str
    description: str
    treasure_rating: int


class Standards_Of_Living(metaclass=MetaEnum):
    POOR = Standard_Of_Living(level=0, name="Poor", 
                              description=("Impoverished folks are probably suffering from a bad harvest season, a fell winter, or the aftermath of a disease or war. "
                                           "They struggle every day to find what they need to survive, and have no time or resources to look for anything beyond "
                                           "the bare necessities, let alone equip themselves for adventure."), 
                              treasure_rating=-30)
    FRUGAL = Standard_Of_Living(level=1, name="Frugal", 
                              description=("Frugal folk usually live off the produce of their own lands and pastures. They wear simple clothes at most times, "
                                           "although they may possess finer garments for special gatherings like seasonal festivals, marriages, or funerals. "
                                           "Any jewels and other superior ornaments are treasured as possessions belonging to the community, and are passed "
                                           "down through generations of appointed keepers. "
                                           "\n\tAdventurers coming from a Frugal folk do not usually carry anything of unusual worth (unless as part of "
                                           "their war gear), with the possible exception of one or two pieces of expensive clothing or common jewellery, "
                                           "like a rich mantle or a golden necklace or bracelet; (probably a token of their status among their peers). "
                                           "Consequently, Frugal Player-heroes can rarely afford to pay for anything, and prefer to find or make what "
                                           "they need instead."), 
                              treasure_rating=0)
    COMMON = Standard_Of_Living(level=2, name="Common", 
                              description=("A folk benefitting from a Common Standard of Living probably hasn’t suffered meaningful setbacks in recent years. "
                                           "Wealth is more widespread than among a Frugal folk, but may be distributed unevenly. Poverty is rare, as is excessive wealth. "
                                           "\n\tPlayer-heroes enjoying a Common Standard of Living have enough resources to look after themselves, and to pay for such "
                                           "things as simple accommodation and meals. Ever mindful of the cost of any luxury, they often lead an austere life, or "
                                           "resort to haggling to lower the price of whatever they are trying to get hold of."), 
                              treasure_rating=30)
    PROSPEROUS = Standard_Of_Living(level=3, name="Prosperous", 
                              description=("Almost all families belonging to a Prosperous Culture can afford to live in separate, private houses. Important "
                                           "individuals wear fine clothing and often have one or two attendants in their service at home, like a gardener "
                                           "and a butler. "
                                           "\n\tPlayer-heroes coming from a Prosperous Culture can usually pay for their share of any out-of-pocket expenses "
                                           "encountered along their journey, and might even pay for another member of the Company, if need be. This includes, "
                                           "for example, paying for comfortable accommodation, spending some time drinking in Company at an inn, and hiring "
                                           "beasts of burden."), 
                              treasure_rating=90)
    RICH = Standard_Of_Living(level=4, name="Rich", 
                              description=("This level of prosperity is usually a transitory condition for a folk, as great wealth can easily attract the "
                                           "attention of many enemies. Members of a Rich Culture live amidst many luxuries, reaping the fruits of a flourishing "
                                           "trade or an extensive treasure. Although those less well-off warn that affluence can easily lead to spiritual or "
                                           "even physical weakness, the availability of material wealth may instead set an individual free to focus on more lofty "
                                           "matters, like the perfection of a trade or art. "
                                           "\n\tRich adventurers fare even better than their Prosperous fellows, but not excessively so. Their life on the move "
                                           "does not let them take full advantage of their resources, as a good proportion of their wealth will be made up of "
                                           "land and riches that are not portable."), 
                              treasure_rating=180)
    VERY_RICH = Standard_Of_Living(level=5, name="Very Rich", 
                              description=("No culture in Middle-earth enjoys this level of prosperity. To reach it, Player-heroes must spend years adventuring, "
                                           "looking for hoards of gold and defeating the creatures jealously guarding them. If they do not die in the attempt, "
                                           "they deserve to spend their remaining years without any monetary concern, as they can afford anything that might take "
                                           "their fancy."), 
                              treasure_rating=300)
    