from dataclasses import dataclass
from utils import MetaEnum


@dataclass
class Calling2():
    name: str
    quote: str
    description: str
    favoured_skills: list[str]
    distinctive_feature: str
    feature_description: str
    shadow_path: str
    shadow_path_description: str


class Callings2(metaclass=MetaEnum):
    CAPTAIN = Calling2(
        name="Captain",
        quote="He stood up, and seemed suddenly to grow taller. In his eyes gleamed a light, keen and commanding.",
        description=("When the world is on the brink of ruin, it is the duty of all individuals of worth to rise and take the lead, whatever the risk. "
                     "You have chosen to put your judgement to the service of others, to guide them in this dark hour. But you don’t want others to heed "
                     "your commands out of fear or obedience — you want them to follow you because they trust you."),
        favoured_skills=["battle", "enhearten", "persuade"],
        distinctive_feature="leadership",
        feature_description="You possess the ability to direct others to action. When under pressure, other people naturally turn to you for guidance.",
        shadow_path="Lure of Power",
        shadow_path_description=("When individuals are given a position of authority, either by rank, lineage, or stature, they may end up mistaking their own "
                                 "aggrandisement for the greater good of the people they should be guiding or keeping safe. Power is the quintessential temptation, "
                                 "and provides the Shadow with an easy way to win the hearts of those who desire it.")
    )
    CHAMPION = Calling2(
        name="Champion",
        quote="“War must be, while we defend our lives against a destroyer who would devour all...”",
        description=("You deem that there is but one way to oppose the return of the Shadow, and that it is to conquer it by strength of arms. "
                     "You are recognised as a warrior among your folk, a valiant fighter, onward into battle. For you, the road to adventure "
                     "leads straight to wherever your foes prowl or hide."),
        favoured_skills=["athletics", "awe", "hunting"],
        distinctive_feature="enemy-lore",
        feature_description=("Enemy-lore is not a single Distinctive Feature; you must select the type of enemies it applies to, choosing from Evil Men, Orcs, "
                             "Spiders, Trolls, Wargs, and Undead. This Distinctive Feature gives you knowledge of the characteristics, habits, strengths, "
                             "and weaknesses of your chosen enemy."),
        shadow_path="Curse of Vengance",
        shadow_path_description=("Individuals who live by the sword are ever tempted to draw it, either literally or figuratively, when their will is "
                                 "thwarted or when they deem their honour to have been impugned by an insult. As corruption spreads in their spirit, "
                                 "their behaviour worsens, leading to more extreme violent reactions.")
    )
    MESSENGER = Calling2(
        name="Messenger",
        quote="“Elrond is sending Elves, and they will get in touch with the Rangers, and maybe with Thranduil’s folk in Mirkwood.”",
        description=("The Wise hold that evil days lie ahead, and that to keep hope, all who fight the Enemy must be as one. Yet, many miles and centuries "
                     "of isolation separate the Free Peoples, and estrange- ment breeds mistrust. You have decided that it is your duty to travel to distant "
                     "lands, carrying tidings and warning people of the coming danger."),
        favoured_skills=["courtesy", "song", "travel"],
        distinctive_feature="folk-lore",
        feature_description=("You possess some knowledge of the many traditional cus- toms, beliefs, and stories of the various communities that compose the "
                             "Free Peoples. Likely the result of your wan- derings, this information may help you when dealing with strangers, "
                             "allowing you to come up with some useful facts regarding their folk or a smattering of the appropriate language."),
        shadow_path="Wandering Madness",
        shadow_path_description=("Travelling afar might be the duty chosen by a messen- ger, but it carries the risk of never finding a place to fight for. "
                                 "The Road goes ever on and on, it’s true, but whither then?")
    )
    SCHOLAR = Calling2(
        name="Scholar",
        quote="“Speak no secrets! Here is a scholar in the Ancient Tongue.”",
        description=("For you, knowledge makes the wild world a less threatening place. Yellowed maps in lost books replace a fear of the unknown with curiosity "
                     "and wonder, songs composed in ages past strengthen the weariest of hearts. A love of learning guides your every step, and illuminates the "
                     "way for you and those who listen to your advice."),
        favoured_skills=["craft", "lore", "riddle"],
        distinctive_feature="Rhymes of Lore"
        shadow_path="Lure of Secrets",
        shadow_path_description=("Inquisitiveness and curiosity are desirable virtues in an individual, but knowledge can be put to malicious use, and learned "
                                 "individuals can look down on others as ignorant fools. Secrets are danger- ous, as the very desire of uncovering them may corrupt the heart.")
    )
    TREASURE_HUNTER = Calling2(
        name="Treasure Hunter",
        quote="Far over the Misty Mountains cold, To dungeons deep and caverns old. We must away ere break of day, To seek the pale enchanted gold.",
        description=("The world has seen the passing of the glory of many Dwar- ven kings and Elven lords, and their heritage is now buried in "
                     "Orc-infested dungeons. Hoards of stolen gold and jewels, guarded by fell beasts, beckon all who dare to find them. "
                     "You seek to recover what is lost, even when it means braving unspeakable dangers."),
        favoured_skills=["explore", "scan", "stealth"],
        distinctive_feature="burglary",
        feature_description=("This venerable talent includes pickpocketing, lock picking and, in general, any shadowy way to get hold "
                             "of the posses- sions of others or access protected areas."),
        shadow_path="Dragon Sickness",
        shadow_path_description=("Adventurers who find themselves on the Road to seek lost riches run the risk of catching the age-old "
                                 "disease capable of turning a pile of enchanted gold into bitter ashes. As the Shadow tightens its grip "
                                 "on their hearts, the world shrinks around them and their closely guarded possessions.")
    )
    WARDEN = Calling2(
        name="Warden",
        quote="“Travellers scowl at us, and countrymen give us scornful names.”",
        description=("In this age of the world, when shadows grow deeper with every passing year, you have sworn to defend all who cannot defend themselves. "
                     "Often, your choice forces you to forsake civilised areas, to better guard their inhabitants from what lurks right outside their fences. "
                     "This has made you a stranger in the eyes of the common folk, a threatening figure like those you are protecting them from."),
        favoured_skills=["awareness", "healing", "insight"],
        distinctive_feature="Shadow-lore",
        feature_description=("You have recognised that there is a hidden thread unifying most of what is malicious, dark, and terrible in Middle-earth, "
                             "and that the thread is thickening year after year. A quality shared by the wise of the land, the truth behind this knowl- edge "
                             "is becoming clearer as time passes."),
        shadow_path="Path of Despair",
        shadow_path_description=("Self-doubt is often the way that the Shadow chooses to reach the heart of those who oppose it. For they know that "
                                 "the Enemy is strong and terrible and that those they protect are too naive or weak to fend for themselves. Every day "
                                 "they ask themselves: strength be enough to prevail, or will I drag down the innocent in defeat?")
    )

    @classmethod
    def by_name(cls, name):
        for calling in Callings2:
            if type(calling) is Calling2:
                if calling.name == name:
                    return calling
    
    @classmethod
    def names(cls):
        names = []
        for calling in Callings2:
            if type(calling) is Calling2:
                names.append(calling.name)
        return names
