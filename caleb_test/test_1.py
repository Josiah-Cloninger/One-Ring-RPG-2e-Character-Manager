import PySimpleGUI as sg
import PIL
from PIL import Image
import threading


from ui_functions import show_attribute, load_character

#cap on scroll
#fix swords and spears in combat proficiencies



def draw_assorted_character_info(active_character, window):
    str_flaws = ", ".join([flaw for flaw in active_character.flaws])
    str_distinctive_features = ", ".join([distinctive_feature for distinctive_feature in active_character.distinctive_features])
    window['-GRAPH-'].draw_text(active_character.name, location=(970, 1000), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.age, location=(675, 938), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.culture, location=(410, 938), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(active_character.blessing.name, location=(410, 903), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.calling, location=(370, 873), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.shadow_path, location=(725, 873), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.patron, location=(690, 903), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.standard_of_living, location=(740, 935), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.treasure, location=(936, 928), color='black', font=("Helvetica", 20), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(str_distinctive_features, location=(990, 935), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(str_flaws, location=(980, 873), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.current_endurance, location=(1383, 510), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.load, location=(1441, 536), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.fatigue, location=(1441, 480), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.current_hope, location=(1530, 510), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.shadow_points, location=(1589, 536), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.shadow_scars, location=(1589, 480), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)


def draw_conditions(active_character, window):
    if active_character.is_weary:
        window['-GRAPH-'].draw_image(r"Square.png", location=(1327, 389))
    if active_character.is_miserable:
        window['-GRAPH-'].draw_image(r"Square.png", location=(1327, 363))
    if active_character.is_wounded:
        window['-GRAPH-'].draw_image(r"Square.png", location=(1327, 337))


def draw_attrabutes(active_character, window):
    window['-GRAPH-'].draw_text(active_character.strength_score, location=(508, 787), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.strength_tn, location=(445, 748), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.max_endurance, location=(508, 710), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.heart_score, location=(842, 785), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.heart_tn, location=(778, 750), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.max_hope, location=(842, 710), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.wits_score, location=(1175, 785), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.wits_tn, location=(1112, 750), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.parry, location=(1175, 710), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)


def draw_skills(active_character, window):
    column_1 = [active_character.awe, active_character.athletics, active_character.awareness, active_character.hunting, active_character.song, active_character.craft]
    column_2 = [active_character.enhearten, active_character.travel, active_character.insight, active_character.healing, active_character.courtesy, active_character.battle]
    column_3 = [active_character.persuade, active_character.stealth, active_character.scan, active_character.explore, active_character.riddle, active_character.lore]
    skill_y_location = 629
    for skill in column_1:
        if skill >= 1:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, skill_y_location))
        if skill >= 2:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, skill_y_location))
        if skill >= 3:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, skill_y_location))
        if skill >= 4:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, skill_y_location))
        if skill >= 5:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, skill_y_location))
        if skill >= 6:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, skill_y_location))
        skill_y_location = skill_y_location - 31.7
    skill_y_location = 629
    for skill in column_2:
        if skill >= 1:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(788, skill_y_location))
        if skill >= 2:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(816, skill_y_location))
        if skill >= 3:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(844, skill_y_location))
        if skill >= 4:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(872, skill_y_location))
        if skill >= 5:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(899, skill_y_location))
        if skill >= 6:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(927, skill_y_location))
        skill_y_location = skill_y_location - 31.7
    skill_y_location = 629
    for skill in column_3:
        if skill >= 1:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(1122, skill_y_location))
        if skill >= 2:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(1150, skill_y_location))
        if skill >= 3:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(1178, skill_y_location))
        if skill >= 4:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(1206, skill_y_location))
        if skill >= 5:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(1233, skill_y_location))
        if skill >= 6:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(1261, skill_y_location))
        skill_y_location = skill_y_location - 31.7


def draw_combat_proficiencies(active_character, window):
    skill_y_location = 375
    for combat_proficiency in active_character.combat_proficiencies:
        if active_character.combat_proficiencies[combat_proficiency] >= 1:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, skill_y_location))
        if active_character.combat_proficiencies[combat_proficiency] >= 2:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, skill_y_location))
        if active_character.combat_proficiencies[combat_proficiency] >= 3:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, skill_y_location))
        if active_character.combat_proficiencies[combat_proficiency] >= 4:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, skill_y_location))
        if active_character.combat_proficiencies[combat_proficiency] >= 5:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, skill_y_location))
        if active_character.combat_proficiencies[combat_proficiency] >= 6:
            window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, skill_y_location))
        skill_y_location = skill_y_location - 31.7


def draw_gear_info(active_character, window):
    try:
        weapon_1_name = active_character.weapons[0].name
        weapon_1_damage = active_character.weapons[0].damage
        weapon_1_injury = active_character.weapons[0].injury
        weapon_1_load = active_character.weapons[0].load
        weapon_1_notes = active_character.weapons[0].notes
    except:
        weapon_1_name = ""
        weapon_1_damage = ""
        weapon_1_injury = ""
        weapon_1_load = ""
        weapon_1_notes = ""
    try:
        weapon_2_name = active_character.weapons[1].name
        weapon_2_damage = active_character.weapons[1].damage
        weapon_2_injury = active_character.weapons[1].injury
        weapon_2_load = active_character.weapons[1].load
        weapon_2_notes = active_character.weapons[1].notes
    except:
        weapon_2_name = ""
        weapon_2_damage = ""
        weapon_2_injury = ""
        weapon_2_load = ""
        weapon_2_notes = ""
    try:
        weapon_3_name = active_character.weapons[2].name
        weapon_3_damage = active_character.weapons[2].damage
        weapon_3_injury = active_character.weapons[2].injury
        weapon_3_load = active_character.weapons[2].load
        weapon_3_notes = active_character.weapons[2].notes
    except:
        weapon_3_name = ""
        weapon_3_damage = ""
        weapon_3_injury = ""
        weapon_3_load = ""
        weapon_3_notes = ""
    try:
        weapon_4_name = active_character.weapons[3].name
        weapon_4_damage = active_character.weapons[3].damage
        weapon_4_injury = active_character.weapons[3].injury
        weapon_4_load = active_character.weapons[3].load
        weapon_4_notes = active_character.weapons[3].notes
    except:
        weapon_4_name = ""
        weapon_4_damage = ""
        weapon_4_injury = ""
        weapon_4_load = ""
        weapon_4_notes = ""
    if active_character.armour != None:
        armour_name = active_character.armour.name
        armour_protection = active_character.armour.protection
        armour_load = active_character.armour.load
    else:
        armour_name = ""
        armour_protection = ""
        armour_load = ""
    if active_character.headgear != None:
        headgear_name = active_character.headgear.name
        headgear_protection = active_character.headgear.protection
        headgear_load = active_character.headgear.load
    else:
        headgear_name = ""
        headgear_protection = ""
        headgear_load = ""
    if active_character.shield != None:
        shield_name = active_character.shield.name
        shield_parry_mod = active_character.shield.parry_mod
        shield_load = active_character.shield.load
    else:
        shield_name = ""
        shield_parry_mod = ""
        shield_load = ""

    window["-GRAPH-"].draw_text(weapon_1_name, location=(330, 175), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_1_damage, location=(530, 185), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_1_injury, location=(584, 185), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_1_load, location=(640, 185), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_1_notes, location=(675, 175), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_2_name, location=(330, 143), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_2_damage, location=(530, 153), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_2_injury, location=(584, 153), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_2_load, location=(640, 153), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_2_notes, location=(675, 143), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_3_name, location=(330, 110), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_3_damage, location=(530, 120), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_3_injury, location=(584, 120), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_3_load, location=(640, 120), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_3_notes, location=(675, 110), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_4_name, location=(330, 77), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(weapon_4_damage, location=(530, 87), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_4_injury, location=(584, 87), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_4_load, location=(640, 87), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(weapon_4_notes, location=(675, 77), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(armour_name, location=(995, 175), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(armour_protection, location=(1200, 185), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(armour_load, location=(1257, 185), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(headgear_name, location=(995, 143), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(headgear_protection, location=(1200, 153), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(headgear_load, location=(1257, 153), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(shield_name, location=(995, 77), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window["-GRAPH-"].draw_text(shield_parry_mod, location=(1200, 87), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)
    window["-GRAPH-"].draw_text(shield_load, location=(1257, 87), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_CENTER)


def draw_points(active_character, window):
    window['-GRAPH-'].draw_text(active_character.adventure_points, location=(1372, 655), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.skill_points, location=(1471, 655), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.fellowship_score, location=(1570, 655), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)


def draw_all(active_character, window):
    draw_assorted_character_info(active_character, window)
    draw_attrabutes(active_character, window)
    draw_skills(active_character, window)
    draw_combat_proficiencies(active_character, window)
    draw_gear_info(active_character, window)
    draw_points(active_character, window)
    draw_conditions(active_character, window)


def show_character_gui(active_character):
    # str_virtues =  ", ".join([virtue for virtue in active_character.virtues])
    # str_rewards = ", ".join([reward for reward in active_character.rewards])
    size = (1920, 1080)
    layout = [
        [sg.Graph(size, (0, 0), size, background_color="black",  expand_x=True, expand_y=True, pad=(0, 0), key='-GRAPH-')]
    ]

    window = sg.Window("Character Sheet", layout, icon=r"Ring_Icon.ico", return_keyboard_events=True, finalize=True, resizable=True, element_justification='c', margins=(0, 0), element_padding=(0,0))
    window['-GRAPH-'].draw_image(r"TOR_Elf_Character_Sheet_fillable (1).png", location=(0, 1080))
    draw_all(active_character, window)
    window.maximize()
    return window


def refresh_character_gui(window):
    window['-GRAPH-'].erase()
    img = Image.open(r"TOR_Elf_Character_Sheet_fillable (1).png")
    img = img.resize(window.size)
    img.save(r"TOR_Elf_Character_Sheet_fillable (2).png")
    window['-GRAPH-'].draw_image(r"TOR_Elf_Character_Sheet_fillable (2).png", location=(0, 1080))
    window['-GRAPH-'].CanvasSize = window.size
    draw_all(active_character, window)
    events, values = window.read()

def scrolling(window):
    index = 0
    up_down_index = 0
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event == "MouseWheel:Up" and up_down_index <= 45:
            window['-GRAPH-'].move(0, -25)
            up_down_index += 1
        if event == "MouseWheel:Down" and up_down_index >= -45:
            window['-GRAPH-'].move(0, 25)
            up_down_index -= 1
        if event == "Up:38" and up_down_index <= 45:
            window['-GRAPH-'].move(0, -25)
            up_down_index += 1
        if event == "Down:40" and up_down_index >= -45:
            window['-GRAPH-'].move(0, 25)
            up_down_index -= 1 
        if event == "Left:37":
            window['-GRAPH-'].move(25, 0)
        if event == "Right:39":
            window['-GRAPH-'].move(-25, 0)
    window.close()

if __name__ == "__main__":
    active_character = load_character("Hithrin")
    window = show_character_gui(active_character)
    t1 = threading.Thread(target=scrolling, args=(window,))
    t2 = threading.Thread(target=refresh_character_gui, args=(window,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    