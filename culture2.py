from utils import MetaEnum
from dataclasses import dataclass


from blessing2 import Blessing2, Blessings2
from standard_of_living import Standards_Of_Living, Standard_Of_Living


@dataclass
class Culture2:
    name: str
    description: str
    characteristics: str
    blessing: Blessing2
    sol: Standard_Of_Living # standard of living
    sol_description: str
    attributes: list

    endurance: int
    hope: int
    parry: int

    skill_levels: dict
    favoured_skills: list
    combat_proficiencies: list

    distinctive_features: list[str]

    langs_and_names: str # languages and names
    male_names: str
    female_names: str
    other_feature: dict = None
    family_names: str=None


class Cultures2(metaclass=MetaEnum):
    BARDING = Culture2(
        name="Bardings",
        description=("\tThe Bardings are Northmen of noble origins hailing from Wilderland, far off to the east. They rebuilt their city of Dale from its "
                     "ashes after the slaying of the Dragon Smaug and they earned a new prosperity trading with nearby kingdoms of Elves and Dwarves. "
                     "\n\tEach year, Barding merchants reach new faraway lands, as they look outside their borders to expand their trade and influence. "
                     "Sometimes, warriors follow in their wake, hoping to prove their mettle against worthy adversaries, inspired by their King\'s "
                     "slaying of the Dragon."),
        characteristics=("\tStrong in body and fearless in spirit, the Northmen are the denizens of Middle-earth that many consider to be nearest in kin "
                         "to the Men of the West. They are strong-limbed, with fair hair, although dark or even black hair is not unknown. Barding men tend to keep "
                         "beards, and often let their hair grow to reach their shoulders. Women adventurers braid their hair in long, tight tresses. "
                         "\n\tBardings rarely become adventurers before their 18th year, and retire in their forties, when they return home to serve their family and folk. "
                         "When abroad they may be recognised by their gear, as they often carry equipment of superior make. Unlike most denizens of Wilderland, "
                         "Bardings prefer to use swords over axes, and naturally favour the bow, after the example of their King."),
        blessing=Blessings2.STOUT_HEARTED,
        sol=Standards_Of_Living.PROSPEROUS,
        sol_description=("Thanks to its successful trading connections the city of Dale prospers. Those among the Bardings who choose a life of adventure "
                         "are usually members of less affluent families — yet, their wealth is still superior to that of most of the denizens of Eriador."),
        attributes=[{"strength": 5, "heart": 7, "wits": 2}, 
                    {"strength": 4, "heart": 7, "wits": 3}, 
                    {"strength": 5, "heart": 6, "wits": 3}, 
                    {"strength": 4, "heart": 6, "wits": 4}, 
                    {"strength": 5, "heart": 5, "wits": 4}, 
                    {"strength": 6, "heart": 6, "wits": 2}],
        endurance=20,
        hope=8,
        parry=12,
        skill_levels={
            "awe": 1, "enhearten": 2, "persuade": 3,
            "athletics": 1, "travel": 1, "stealth": 0,
            "awareness": 0, "insight": 2, "scan": 1,
            "hunting": 2, "healing": 0, "explore": 1,
            "song": 1, "courtesy": 2, "riddle": 0,
            "craft": 1, "battle": 2, "lore": 1
        },
        favoured_skills=["enhearten", "athletics"],
        combat_proficiencies=["bows", "swords"],
        distinctive_features=["Bold", "Eager", "Fair", "Fierce", "Generous", "Proud", "Tall", "Wilful"],
        langs_and_names=("All Bardings speak Dalish, a language that can be described as a very old form of the Common Speech. As far as their names are concerned, "
                         "they are usually composed of one or two elements (for example, Dag — Day, or Lif-stan — Life Stone). Like most Northmen, Bardings often name their children "
                         "after a renowned ancestor or relative, or choose a name beginning with the same sound or sharing one element with that of the father (whose name is often "
                         "given with their first name when introduced formally — for example, Lifstan, son of Leiknir, or Ingrith, daughter of Ingolf)."),
        male_names=("Aegir, Arn, Brandulf, Domarr, Egil, Erland, Farald, Finn, Gautarr, Hafgrim, Hjalmar, Ingolf, Jofur, Kolbeinn, Leiknir, Lomund, "
                    "Munan, Nari, Nefstan, Ottarr, Ragnarr, Reinald, Sigmarr, Steinarr, Thorald, Torwald, Ulfarr, Unnarr, Vandil, Varinn."),
        female_names=("Aldis, Asfrid, Bera, Bergdis, Dagmar, Eilif, Erna, Frida, Geira, Gudrun, Halla, Hild, Ingirun, Ingrith, Lif, Linhild, "
                      "Kelda, Runa, Saldis, Sigga, Sigrun, Thora, Thordis, Thorhild, Ulfhild, Ulfrun, Una, Valdis, Vigdis, Walda.")
    )
    DWARF = Culture2(
        name="Dwarves of Durins Folk",
        description=("\tThe Dwarves are an ancient and proud folk, whose customs and traditions are mostly unknown to outsiders. A dwindling people, they have "
                     "recently recovered some of their lost greatness, and a Dwarven King reigns once again under the Lonely Mountain, in Wilderland. "
                     "\n\tMany Dwarves cross into Eriador from the East, on their way to their mines in the Blue Mountains. They can often be seen marching "
                     "along the East-West Road that runs through the Shire and ends at the Grey Havens."),
        characteristics=("he Dwarves are exceedingly strong for their height, and hard to break or corrupt, but often at odds with other folks over old quarrels "
                         "or new slights. They are short and stocky, with robust limbs and heads crowned with long hair and longer beards that give them their "
                         "typically elderly appearance. When on a journey or in battle they plait their forked beards and thrust them into their belts. "
                         "Dwarves generally start their life on the road in their fifties, and do not usually consider retiring before their nineties. Around that "
                         "time, many among them choose to dedicate themselves solely to the perfection of their crafts. In battle most Dwarves use axes and swords, "
                         "but those belonging to their easternmost kin wield heavy two-handed mattocks, a weapon derived from their mining tools."),
        blessing=Blessings2.REDOUBTABLE,
        other_feature={
            "name": "Naugrim",
            "flavour": ("Dwarves are shorter than Men, but their work as miners and smiths endows them with powerful arms and shoulders. "
                        "Yet,they still favour shorter weapons over longer ones."),
            "effect": "Dwarven adventurers cannot use the following pieces of war gear: great bow, great spear, long sword, and great shield."
        },
        sol=Standards_Of_Living.PROSPEROUS,
        sol_description="With the fabulous Dragon-hoard of Erebor reclaimed and their kingdom restored, the Dwarves are much richer today than in the past.",
        attributes=[{"strength": 7, "heart": 2, "wits": 5}, 
                    {"strength": 7, "heart": 3, "wits": 4}, 
                    {"strength": 6, "heart": 3, "wits": 5}, 
                    {"strength": 6, "heart": 4, "wits": 4}, 
                    {"strength": 5, "heart": 4, "wits": 5}, 
                    {"strength": 6, "heart": 2, "wits": 6}],
        endurance=22,
        hope=8,
        parry=10,
        skill_levels={
            "awe": 2, "enhearten": 0, "persuade": 0,
            "athletics": 1, "travel": 3, "stealth": 0,
            "awareness": 0, "insight": 0, "scan": 3,
            "hunting": 0, "healing": 0, "explore": 2,
            "song": 1, "courtesy": 1, "riddle": 2,
            "craft": 2, "battle": 1, "lore": 1
        },
        favoured_skills=["travel", "craft"],
        combat_proficiencies={"axes", "swords"},
        distinctive_features=["Cunning", "Fierce", "Lordly", "Proud", "Secretive", "Stern", "Wary", "Wilful"],
        langs_and_names=("All Dwarves speak the Common Tongue, but preserve a knowledge of a secret Dwarvish language. They receive a true name at birth that "
                         "they do not reveal to members of other folks, and adopt another name in the tradition of their neighbours. This custom has been in use "
                         "for so long that a number of names have become traditionally associated with Dwarves, and are used almost exclusively by them. Dwarves of "
                         "renown are sometimes given an honorific title, celebrating an exceptional deed or distinctive quality (for example, Thorin Oakenshield or "
                         "Dáin Ironfoot)."),
        male_names=("Ai, Anar, Beli, Bláin, Borin, Burin, Bruni, Farin, Flói, Frár, Frerin, Frór, Ginar, Gróin, Grór, Hanar, "
                    "Hepti, Iari, Lófar, Lóni, Náli, Nár, Niping, Nói, Núr, Nýrád, Ónar, Póri, Regin, Svior, Veig, Vidar."),
        female_names=("Adís, Afrid, Agda, Bersa, Birna, Dagrún, Dís, Drífa, Edda, Elin, Fenja, Frida, Geira, Gísla, Hadda, Hón, Ida, Ilmr, "
                      "Jóra, Kára, Kóna, Líf, Línhild, Már, Mist, Nál, Oda, Ósk, Rán, Rinda, Sefa, Syn, Tóra, Trana, Úlfrún, Vírún, Yrr.")
    )
    ELF = Culture2(
        name="Elves of Lindon",
        description=("The Fair Folk of Eriador have dwelt in the Westlands since before the drowning of Beleriand. They are all members of the Firstborn, "
                     "displaying a wisdom beyond the reach of Men. They rarely leave their sanctuaries in the Grey Havens, for these are their fading years. "
                     "\n\tMore and more leave Middle-earth sailing West on grey ships, never to return. Those who still remain live mostly along the western coasts, "
                     "where once were found great kingdoms of their kindreds. Wandering Elves can at times be encountered on the roads leading east in spring "
                     "and autumn, when their companies leave their lands beyond the Tower Hills."),
        characteristics=("All Elves are endowed with tremendous vitality and great vigour. They are not subject to illness or old age, and thus can dwell within "
                         "the circles of the world until they choose to leave it, or are slain. Elves may leave their homes at any time after they reach adulthood "
                         "(at about a century of age). Adventurers older than 300 years are rare, as in time all Elves find the sea-longing that lies deep within "
                         "their hearts to become irresistible. In battle, most Elves carry bows and spears. Many wield swords too, but by ancient tradition some "
                         "still favour axes."),
        blessing=Blessings2.ELVEN_SKILL,
        other_feature={
            "name": "The Long Defeat",
            "flavour": "The Elves find it hard to forget the taint of the Shadow once it has left its mark on their spirit.",
            "effect": "When it is time to remove accumulated Shadow during the Fellowship Phase, you can only remove a maximum of 1 point (see Spiritual Recovery, page 119)."
        },
        sol=Standards_Of_Living.FRUGAL,
        sol_description=("The Fair Folk live in harmony with Middle-earth and have little or no use for those things that others consider precious. They lack "
                         "nothing, and craft beautiful things using the richest materials, but they don’t profit from their wealth the way other folks do."),
        attributes=[{"strength": 5, "heart": 2, "wits": 7}, 
                    {"strength": 4, "heart": 3, "wits": 7}, 
                    {"strength": 5, "heart": 3, "wits": 6}, 
                    {"strength": 4, "heart": 4, "wits": 6}, 
                    {"strength": 5, "heart": 4, "wits": 5}, 
                    {"strength": 6, "heart": 2, "wits": 6}],
        endurance=20,
        hope=8,
        parry=12,
        skill_levels={
            "awe": 2, "enhearten": 1, "persuade": 0,
            "athletics": 2, "travel": 0, "stealth": 3,
            "awareness": 2, "insight": 0, "scan": 0,
            "hunting": 0, "healing": 1, "explore": 0,
            "song": 2, "courtesy": 0, "riddle": 0,
            "craft": 2, "battle": 1, "lore": 3
        },
        favoured_skills=["song", "lore"],
        combat_proficiencies=["bows", "spears"],
        distinctive_features=["Fair", "Keen-eyed", "Lordly", "Merry", "Patient", "Subtle", "Swift", "Wary"],
        langs_and_names=("In addition to the Common Speech, all Elves speak their own, fair tongue — the Sindarin speech. For the most part, the Elves of Lindon bear "
                         "names fashioned in that language."),
        male_names=("Amras, Aredhel, Beleganor, Belegon, Calanhir, Carmagor, Dagorhir, Durandir, Edrahil, Ellahir, Fincalan, Fuindor, Galdagor, Galdor, "
                    "Hallas, Hirimlad, Ithildir, Lascalan, Linaith, Mablin, Malanor, Nauros, Orgalad, Pelegorn, Sargon."),
        female_names=("Aranel, Arbereth, Berúthiel, Baraniel, Calanril, Celenneth, Elnîth, Eraniel, Finduilas, Gilraen, Gilraeth, Gloredhel, Idril, "
                      "Ioreth, Ivorwen, Lôrwend, Lothíriel, Luindîs, Meneloth, Moriel, Morwen, Narieth, Narniel, Orothêl, Tarandîs.")
    )
    HOBBIT = Culture2(
        name="Hobbits of the Shire",
        description=("Hobbits are a small and merry folk, possessing a love for time-honoured traditions and respectable ways, and a strong dislike for anything "
                     "out of the ordinary. If Hobbits had their way, the days would go by in an unchanging world, as they have since anyone can remember. At least, "
                     "in their land, the Shire. "
                     "\n\tBut since the return of Mr Bilbo Baggins from his adventure with a group of Dwarves and a travelling Wizard, something has changed. "
                     "Stories about remote lands, dark woods, Giants, Elves, and forgotten halls beneath the earth have started to circulate among Hobbits "
                     "of a more adventurous sort. And with every year, another one or two discreetly disappear to go and have adventures."),
        characteristics=("Hobbits are much smaller than Men, even smaller than Dwarves, and might be mistaken for children of Men by those who do not know "
                         "of their existence. They have never been warlike, but for all their gentle appearance they are surprisingly tough, and difficult to "
                         "intimidate or kill. A merry folk, Hobbits possess a cheerful spirit and a friendliness that makes them good companions. "
                         "\n\tHobbits do not abandon their comfortable lives easily, but when they do they usually wait for their coming of age at 33. "
                         "A particularly reckless fellow might feel the call to adventure when in their tweens, as Hobbits call their twenties. "
                         "When pushed to resort to weapons, Hobbits choose short swords and hunting bows, which they can shoot with uncanny precision."),
        blessing=Blessings2.HOBBIT_SENSE,
        other_feature={
            "name": "Halflings",
            "flavour": "Due to their reduced size, Hobbits cannot use larger weapons effectively. The weapons available to Hobbits are:",
            "effect": "Axe, bow, club, cudgel, dagger, short sword, short spear, spear. Additionally, Hobbits cannot use a great shield."
        },
        sol=Standards_Of_Living.COMMON,
        sol_description=("Hobbits live in peace, their land is well-tilled and their borders protected, but theirs is an isolated "
                        "island in the middle of a desolate region, and trading is an uncommon occurrence."),
        attributes=[{"strength": 3, "heart": 6, "wits": 5}, 
                    {"strength": 3, "heart": 7, "wits": 4}, 
                    {"strength": 2, "heart": 7, "wits": 5}, 
                    {"strength": 4, "heart": 6, "wits": 4}, 
                    {"strength": 4, "heart": 5, "wits": 5}, 
                    {"strength": 2, "heart": 6, "wits": 6}],
        endurance=18,
        hope=10,
        parry=12,
        skill_levels={
            "awe": 0, "enhearten": 0, "persuade": 2,
            "athletics": 0, "travel": 0, "stealth": 3,
            "awareness": 2, "insight": 0, "scan": 0,
            "hunting": 0, "healing": 1, "explore": 0,
            "song": 2, "courtesy": 1, "riddle": 3,
            "craft": 1, "battle": 0, "lore": 0
        },
        favoured_skills=["stealth", "courtesy"],
        combat_proficiencies=["axes", "bows"],
        distinctive_features=["Eager", "Fair-spoken", "Faithful", "Honourable", "Inquisitive", "Keen-eyed", "Merry", "Rustic"],
        langs_and_names=("Hobbits speak only the Common Speech, preserving the use of a few words and names of their own forgotten tongue. Names are composed "
                         "of a first name and a family name. First names for men are usually simple and short, with women being often given names of flowers "
                         "or precious stones, but among the older families a custom survives of giving more heroic and high-sounding names, whose origin can "
                         "be traced back to a time before the Shire."),
        male_names=("Andwise, Berilac, Bungo, Cottar, Doderic, Dudo, Erling, Fastred, Ferumbras, Folco, Gorhendad, Griffo, Halfred, Hamson, Ilberic, "
                    "Isembold, Isengar, Longo, Marmadas, Marroc, Mungo, Odo, Orgulas, Otho, Posco, Reginard, Robin, Rudigar, Sadoc, Saradas, Tobold, Tolman."),
        female_names=("Adaldrida, Amaranth, Asphodel, Belba, Bell, Berylla, Camellia, Daisy, Eglantine, Estella, Gilly, Hanna, Lily, Malva, Marigold, May, Melilot, "
                      "Menegilda, Mentha, Mirabella, Myrtle, Pearl, Peony, Pervinca, Pimpernel, Primrose, Primula, Prisca, Rosamunda, Ruby, Salvia."),
        family_names=("Baggins, Boffin, Bolger, Bracegirdle, Brandybuck, Brown, Brownlock, Bunce, Burrows, Cotton, Gamgee, Gardner, Goldworthy, Goodbody, "
                      "Goodchild, Grubb, Headstrong, Hornblower, Maggot, Noakes, North-Tooks, Proudfoot, Puddifoot, Roper, Rumble, Sackville, Smallburrow, "
                      "Took, Twofoot, Whitfoot.")
    )
    MAN_OF_BREE = Culture2(
        name="Men of Bree",
        description=("The inhabitants of the Bree-land and its four villages lying about Bree-hill are the descendants of the ancient people that first dwelt in the region known today as Eriador, the Lonelands. Few have survived the turmoils that have ravaged the area, but they are still there now. Today, the Men of Bree live at an old meeting of ways, and even if the traffic was far greater in former days, travellers of various sorts still make their way along those roads. Whoever enters the common room of the Inn of Bree is sure to hear strange tales and news from afar, and maybe be swept away by them."),
        characteristics=("Most Men of Bree are brown-haired and rather short, and tend to be stocky and broad. This, combined with their cheerful disposition, "
                         "is the reason why they do not appear as outlandish as most foreigners do to their neighbours, the inhabitants of the Shire. But "
                         "like Hobbits, their appearance can be deceiving: the Men of Bree can be simple and friendly, but they are independent and wise in their own way. "
                         "\n\tActual adventurers from Bree-land are rare indeed. If they leave their villages at all, they do it when the vigour of youth is "
                         "in their limbs, and usually return home to settle down before their fortieth year. Not being of a warlike disposition, the Bree-folk "
                         "favour simple weapons, derived from everyday tools and hunting implements."),
        blessing=Blessings2.BREE_BLOOD,
        sol=Standards_Of_Living.COMMON,
        sol_description=("Bree-land is not as wealthy as it once was, but these days the inhabitants of the four villages are no "
                         "more rustic than their neighbours in the Shire, and no less well-off."),
        attributes=[{"strength": 2, "heart": 5, "wits": 7}, 
                    {"strength": 3, "heart": 4, "wits": 7}, 
                    {"strength": 3, "heart": 5, "wits": 6}, 
                    {"strength": 4, "heart": 4, "wits": 6}, 
                    {"strength": 4, "heart": 5, "wits": 5}, 
                    {"strength": 2, "heart": 6, "wits": 6}],
        endurance=20,
        hope=10,
        parry=10,
        skill_levels={
            "awe": 0, "enhearten": 2, "persuade": 2,
            "athletics": 1, "travel": 1, "stealth": 1,
            "awareness": 1, "insight": 2, "scan": 1,
            "hunting": 1, "healing": 0, "explore": 1,
            "song": 1, "courtesy": 3, "riddle": 2,
            "craft": 2, "battle": 0, "lore": 0
        },
        favoured_skills=["insight", "riddle"],
        combat_proficiencies=["axes", "spears"],
        distinctive_features=["Cunning", "Fair-spoken", "Faithful", "Generous", "Inquisitive", "Patient", "Rustic", "True-hearted"],
        langs_and_names=("The Men of Bree have forgotten their ancient, native speech, and speak the Common Tongue, albeit slightly altered in a local dialect. "
                         "They use names that to foreign ears sound similar to those used by Hobbits in the Shire (Hobbits beg to differ, of course)."),
        male_names=("Alfred, Artie, Bill, Bob, Carl, Ed, Fred, Giles, Herb, Larry, Nob, Oswald, Percy, Perry, Sid, Tom, Harry"),
        female_names=("Daisy, Emma, Etta, Fay, Fern, Flora, Gert, Holly, Lily, Myrtle, Poppy, Rose, Sage, Tilly, Violet."),
        family_names=("Appledore, Asterfire, Bellsap, Briarcleave, Butterbur, Cherryborn, Chesterstout, Droverwind, Ferny, Foxglow, Goatleaf, "
                      "Hardybough, Heathertoes, Hedgedon, Kettlegrass, Lilyhawk, Mossburn, Mugworts, Oakstout, Pickthorn, Pollenroad, Rushlight, "
                      "Shrubrose, Sweetroot, Thistlewool, Wayward.")
    )
    RANGER = Culture2(
        name="Rangers of the North",
        description=("The Rangers of the North are a secret people, severely dimin- ished in number with the passing of a thousand years. They wander in disguise "
                     "among the ruins of what was once their kingdom of Arnor, tirelessly patrolling its many paths and roads. "
                     "\n\tWhile the years have lengthened, the task of the Rangers has always been the same: to keep the folk of Eriador free from care and fear. "
                     "They labour secretly, keeping to them- selves, and rarely giving their names to the travellers they save or to the folk whose farms they "
                     "guard at night, when evil thingscome out from dark places."),
        characteristics=("The Rangers are the last descendants in the North of the Dúnedain, kings among Men that once came to Middle-earth over the Sea out of "
                         "Westernesse. When they do not disguise their features, they are tall and lordly, towering above most Men. They are often silent and "
                         "grim of countenance, and look wise and mature beyond their years. "
                         "Rangers take to the Wild around the age of twenty, but may begin to go on adventures even at a younger age. They retain their strength "
                         "of body and will longer than most Men, but usually cease to travel far from Eriador when they reach their fifties. When in the Wild, "
                         "they wear comfortable but weather-beaten garments, favouring high leather boots and heavy cloaks of dark grey or green cloth, with "
                         "ample hoods that can be cast over a worn helm."),
        blessing=Blessings2.KINGS_OF_MEN,
        other_feature={
            "name": "Allegiance of the Dúnedain",
            "flavour": ("The Rangers are devoted to fighting Sauron and his min- ions by an ancient tradition of war and strife. "
                        "This obligation makes it harder for them to put their spirit at ease even when enjoying a respite from adventuring."),
            "effect": "During the Fellowship phase (not Yule) you recover a maximum number of Hope points equal to half your HEART score (rounding fractions up)."
        },
        sol=Standards_Of_Living.FRUGAL,
        sol_description=("Rangers rarely wear or carry anything whose worth cannot be measured in a practical way. Their gear or garments are never considered "
                         "precious for the gleam of stone or gold, but for their capability to endure long journeys and strenuous fights."),
        attributes=[{"strength": 7, "heart": 5, "wits": 2}, 
                    {"strength": 7, "heart": 4, "wits": 3}, 
                    {"strength": 6, "heart": 5, "wits": 3}, 
                    {"strength": 6, "heart": 4, "wits": 4}, 
                    {"strength": 5, "heart": 5, "wits": 4}, 
                    {"strength": 6, "heart": 6, "wits": 2}],
        endurance=20,
        hope=6,
        parry=14,
        skill_levels={
            "awe": 1, "enhearten": 0, "persuade": 0,
            "athletics": 2, "travel": 2, "stealth": 2,
            "awareness": 2, "insight": 0, "scan": 1,
            "hunting": 2, "healing": 2, "explore": 2,
            "song": 0, "courtesy": 0, "riddle": 0,
            "craft": 0, "battle": 2, "lore": 2
        },
        favoured_skills=["hunting", "lore"],
        combat_proficiencies=["spears", "swords"],
        distinctive_features=["Bold", "Honourable", "Secretive", "Stern", "Subtle", "Swift", "Tall", "True-hearted"],
        langs_and_names=("The native language of the Dúnedain is the Westron, or Common Speech. Some still learn the Sindarin Elven-tongue, as it is handed "
                         "down from generation to generation. They retain an ancient tradition of naming their children using that fair speech."),
        male_names=("Adrahil, Amlaith, Arvegil, Baranor, Belecthor, Bergil, Celepharn, Cirion, Damrod, Dírhael, Duinhir, Egalmoth, Eradan, "
                    "Findemir, Forlong, Golasdan, Hallas, Hirluin, Ingold, Iorlas, Malvegil, Ohtar, Orodreth, Tarannon, Targon."),
        female_names=("Anwen, Arbereth, Berúthiel, Baraniel, Calanril, Celenneth, Elnîth, Eraniel, Finduilas, Gilraen, Gilraeth, Gloredhel, "
                      "Idril, Ioreth, Ivorwen, Lôrwend, Lothíriel, Luindîs, Meneloth, Moriel, Morwen, Narieth, Narniel, Orothêl, Tarandîs.")
    )

    @classmethod
    def by_name(cls, name):
        for culture in Cultures2:
            if type(culture) is Culture2:
                if culture.name == name:
                    return culture
    
    @classmethod
    def names(cls):
        names = []
        for culture in Cultures2:
            if type(culture) is Culture2:
                names.append(culture.name)
        return names

all_combat_proficiencies = ["axes", "bows", "spears", "swords"]