import PySimpleGUI as sg
import time


from ui_functions import show_attribute, load_character

#cap on scroll


def create_layout():
    active_character = load_character("Lif")
    print(active_character)

    str_flaws = ", ".join([flaw for flaw in active_character.flaws])
    str_virtues =  ", ".join([virtue for virtue in active_character.virtues])
    str_rewards = ", ".join([reward for reward in active_character.rewards])
    str_distinctive_features = ", ".join([distinctive_feature for distinctive_feature in active_character.distinctive_features])

    try:
        weapon_1_name = active_character.weapons[0].name
        weapon_1_damage = active_character.weapons[0].damage
        weapon_1_injury = active_character.weapons[0].injury
        weapon_1_load = active_character.weapons[0].load
        weapon_1_notes = active_character.weapons[0].notes
    except:
        weapon_1_name = None
        weapon_1_damage = None
        weapon_1_injury = None
        weapon_1_load = None
        weapon_1_notes = None
    try:
        weapon_2_name = active_character.weapons[1].name
        weapon_2_damage = active_character.weapons[1].damage
        weapon_2_injury = active_character.weapons[1].injury
        weapon_2_load = active_character.weapons[1].load
        weapon_2_notes = active_character.weapons[1].notes
    except:
        weapon_2_name = None
        weapon_2_damage = None
        weapon_2_injury = None
        weapon_2_load = None
        weapon_2_notes = None
    try:
        weapon_3_name = active_character.weapons[2].name
        weapon_3_damage = active_character.weapons[2].damage
        weapon_3_injury = active_character.weapons[2].injury
        weapon_3_load = active_character.weapons[2].load
        weapon_3_notes = active_character.weapons[2].notes
    except:
        weapon_3_name = None
        weapon_3_damage = None
        weapon_3_injury = None
        weapon_3_load = None
        weapon_3_notes = None
    try:
        weapon_4_name = active_character.weapons[3].name
        weapon_4_damage = active_character.weapons[3].damage
        weapon_4_injury = active_character.weapons[3].injury
        weapon_4_load = active_character.weapons[3].load
        weapon_4_notes = active_character.weapons[3].notes
    except:
        weapon_4_name = None
        weapon_4_damage = None
        weapon_4_injury = None
        weapon_4_load = None
        weapon_4_notes = None
    if active_character.armour is not None:
        armour_name = active_character.armour.name
        armour_protection = active_character.armour.protection
        armour_load = active_character.armour.load
    else:
        armour_name = None
        armour_protection = None
        armour_load = None
    if active_character.headgear is not None:
        headgear_name = active_character.headgear.name
        headgear_protection = active_character.headgear.protection
        headgear_load = active_character.headgear.load
    else:
        headgear_name = None
        headgear_protection = None
        headgear_load = None
    if active_character.shield is not None:
        shield_name = active_character.shield.name
        shield_parry_mod = active_character.shield.parry_mod
        shield_load = active_character.shield.load
    else:
        shield_name = None
        shield_parry_mod = None
        shield_load = None


    character_info = {
        "name" : sg.Text(active_character.name),
        "age" : sg.Text(active_character.age),
        "culture" : sg.Text(active_character.culture),
        "calling" : sg.Text(active_character.calling),
        "shadow_path" : sg.Text(active_character.shadow_path),
        "patron" : sg.Text(active_character.patron),
        "standard_of_living" : sg.Text(active_character.standard_of_living),
        "treasure" : sg.Text(active_character.treasure),
        "distinctive_features" : sg.Text(str_distinctive_features),
        "flaws" : sg.Text(str_flaws),
        "strength_score" : sg.Text(active_character.strength_score),
        "strength_tn" : sg.Text(active_character.strength_tn),
        "max_endurance" : sg.Text(active_character.max_endurance),
        "current_endurance" : sg.Text(active_character.current_endurance),
        "heart_score" : sg.Text(active_character.heart_score),
        "heart_tn" : sg.Text(active_character.heart_tn),
        "max_hope" : sg.Text(active_character.max_hope),
        "current_hope" : sg.Text(active_character.current_hope),
        "wits_score" : sg.Text(active_character.wits_score),
        "wits_tn" : sg.Text(active_character.wits_tn),
        "parry" : sg.Text(active_character.parry),
        "awe" : sg.Text(active_character.awe),
        "athletics" : sg.Text(active_character.athletics),
        "awareness" : sg.Text(active_character.awareness),
        "hunting" : sg.Text(active_character.hunting),
        "song" : sg.Text(active_character.song),
        "craft" : sg.Text(active_character.craft),
        "enhearten" : sg.Text(active_character.enhearten),
        "travel" : sg.Text(active_character.travel),
        "insight" : sg.Text(active_character.insight),
        "healing" : sg.Text(active_character.healing),
        "courtesy" : sg.Text(active_character.courtesy),
        "battle" : sg.Text(active_character.battle),
        "persuade" : sg.Text(active_character.persuade),
        "stealth" : sg.Text(active_character.stealth),
        "scan" : sg.Text(active_character.scan),
        "explore" : sg.Text(active_character.explore),
        "riddle" : sg.Text(active_character.riddle),
        "lore" : sg.Text(active_character.lore),
        "axes_skill" : sg.Text(active_character.axes_skill),
        "bows_skill" : sg.Text(active_character.bows_skill),
        "swords_skill" : sg.Text(active_character.swords_skill),
        "spears_skill" : sg.Text(active_character.spears_skill),
        "virtues" : sg.Text(str_virtues),
        "rewards" : sg.Text(str_rewards),
        "weapon_1_name" : sg.Text(weapon_1_name),
        "weapon_1_damage" : sg.Text(weapon_1_damage),
        "weapon_1_injury" : sg.Text(weapon_1_injury),
        "weapon_1_load" : sg.Text(weapon_1_load),
        "weapon_1_notes" : sg.Text(weapon_1_notes),
        "weapon_2_name" : sg.Text(weapon_2_name),
        "weapon_2_damage" : sg.Text(weapon_2_damage),
        "weapon_2_injury" : sg.Text(weapon_2_injury),
        "weapon_2_load" : sg.Text(weapon_2_load),
        "weapon_2_notes" : sg.Text(weapon_2_notes),
        "weapon_3_name" : sg.Text(weapon_3_name),
        "weapon_3_damage" : sg.Text(weapon_3_damage),
        "weapon_3_injury" : sg.Text(weapon_3_injury),
        "weapon_3_load" : sg.Text(weapon_3_load),
        "weapon_3_notes" : sg.Text(weapon_3_notes),
        "weapon_4_name" : sg.Text(weapon_4_name),
        "weapon_4_damage" : sg.Text(weapon_4_damage),
        "weapon_4_injury" : sg.Text(weapon_4_injury),
        "weapon_4_load" : sg.Text(weapon_4_load),
        "weapon_4_notes" : sg.Text(weapon_4_notes),
        "armour_name" : sg.Text(armour_name),
        "armour_protection" : sg.Text(armour_protection),
        "armour_load" : sg.Text(armour_load),
        "headgear_name" : sg.Text(headgear_name),
        "headgear_protection" : sg.Text(headgear_protection),
        "headgear_load" : sg.Text(headgear_load),
        "shield_name" : sg.Text(shield_name),
        "shield_parry_mod" : sg.Text(shield_parry_mod),
        "shield_load" : sg.Text(shield_load),
        "adventure_points" : sg.Text(active_character.adventure_points),
        "skill_points" : sg.Text(active_character.skill_points),
        "fellowship_score" : sg.Text(active_character.fellowship_score),
        "load" : sg.Text(active_character.load),
        "fatigue" : sg.Text(active_character.fatigue),
        "shadow_points" : sg.Text(active_character.shadow_points),
        "shadow_scars" : sg.Text(active_character.shadow_scars),
        "is_weary" : sg.Text(active_character.is_weary),
        "is_miserable" : sg.Text(active_character.is_miserable),
        "is_wounded" : sg.Text(active_character.is_wounded),
        "injury" : sg.Text(active_character.injury),
    }


def draw_awe(active_character, window):
    if active_character.awe == 0:
        pass
    if active_character.awe >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, 629))
    if active_character.awe >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, 629))
    if active_character.awe >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, 629))
    if active_character.awe >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, 629))
    if active_character.awe >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, 629))
    if active_character.awe >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, 629))


def draw_athletics(active_character, window):
    if active_character.athletics == 0:
        pass
    if active_character.athletics >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, 598))
    if active_character.athletics >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, 598))
    if active_character.athletics >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, 598))
    if active_character.athletics >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, 598))
    if active_character.athletics >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, 598))
    if active_character.athletics >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, 598))


def draw_awareness(active_character, window):
    if active_character.awareness == 0:
        pass
    if active_character.awareness >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, 565))
    if active_character.awareness >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, 565))
    if active_character.awareness >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, 565))
    if active_character.awareness >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, 565))
    if active_character.awareness >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, 565))
    if active_character.awareness >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, 565))


def draw_hunting(active_character, window):
    if active_character.hunting == 0:
        pass
    if active_character.hunting >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, 534))
    if active_character.hunting >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, 534))
    if active_character.hunting >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, 534))
    if active_character.hunting >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, 534))
    if active_character.hunting >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, 534))
    if active_character.hunting >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, 534))


def draw_song(active_character, window):
    if active_character.song == 0:
        pass
    if active_character.song >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, 502))
    if active_character.song >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, 502))
    if active_character.song >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, 502))
    if active_character.song >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, 502))
    if active_character.song >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, 502))
    if active_character.song >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, 502))


def draw_craft(active_character, window):
    if active_character.craft == 0:
        pass
    if active_character.craft >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(454, 470))
    if active_character.craft >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(482, 470))
    if active_character.craft >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(510, 470))
    if active_character.craft >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(538, 470))
    if active_character.craft >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(565, 470))
    if active_character.craft >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(593, 470))


def draw_enhearten(active_character, window):
    if active_character.enhearten == 0:
        pass
    if active_character.enhearten >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(788, 629))
    if active_character.enhearten >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(816, 629))
    if active_character.enhearten >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(844, 629))
    if active_character.enhearten >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(872, 629))
    if active_character.enhearten >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(899, 629))
    if active_character.enhearten >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(927, 629))


def test(active_character, window):
    column_1 = [active_character.awe, active_character.athletics, active_character.awareness, active_character.hunting, active_character.song, active_character.craft]
    column_2 = [active_character.enhearten, active_character.travel, active_character.insight, active_character.healing, active_character.courtsey, active_character.battle]
    column_3 = [active_character.persuade, active_character.stealth, active_character.scan, active_character.explore, active_character.riddle, active_character.lore]
    for skill in column_1:
        if skill is 



def draw_travel(active_character, window):
    if active_character.travel == 0:
        pass
    if active_character.travel >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(788, 598))
    if active_character.travel >= 2:        
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(816, 598))
    if active_character.travel >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(844, 598))
    if active_character.travel >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(872, 598))
    if active_character.travel >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(899, 598))
    if active_character.travel >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(927, 598))


def draw_insight(active_character, window):
    if active_character.insight == 0:
        pass
    if active_character.insight >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(788, 565))
    if active_character.insight >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(816, 565))
    if active_character.insight >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(844, 565))
    if active_character.insight >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(872, 565))
    if active_character.insight >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(899, 565))
    if active_character.insight >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(927, 565))


def draw_healing(active_character, window):
    if active_character.healing == 0:
        pass
    if active_character.healing >= 1:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(788, 534))
    if active_character.healing >= 2:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(816, 534))
    if active_character.healing >= 3:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(844, 534))
    if active_character.healing >= 4:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(872, 534))    
    if active_character.healing >= 5:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(899, 534))
    if active_character.healing >= 6:
        window["-GRAPH-"].draw_image(r"Rombus.png", location=(927, 534))


def draw_skills(active_character, window):
    draw_awe(active_character, window)
    draw_athletics(active_character, window)
    draw_awareness(active_character, window)
    draw_hunting(active_character, window)
    draw_song(active_character, window)
    draw_craft(active_character, window)
    draw_enhearten(active_character, window)
    draw_travel(active_character, window)
    draw_insight(active_character, window)
    draw_healing(active_character, window)


def main():
    active_character = load_character("Arathorn")
    str_flaws = ", ".join([flaw for flaw in active_character.flaws])
    str_virtues =  ", ".join([virtue for virtue in active_character.virtues])
    str_rewards = ", ".join([reward for reward in active_character.rewards])
    str_distinctive_features = ", ".join([distinctive_feature for distinctive_feature in active_character.distinctive_features])

    layout = [
        [sg.Graph(canvas_size=(1920, 1080), background_color="black", graph_bottom_left=(0, 0), graph_top_right=(1920, 1080), expand_x=True, expand_y=True, change_submits=True, drag_submits=True, key='-GRAPH-')]
    ]

    window = sg.Window("Character Sheet", layout, return_keyboard_events=True, finalize=True, resizable=True, element_justification='c', margins=(0, 0), element_padding=(0,0))
    window['-GRAPH-'].draw_image(r"TOR_Elf_Character_Sheet_fillable (1).png", location=(0, 1080))
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
    window['-GRAPH-'].draw_text(active_character.strength_score, location=(508, 787), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.strength_tn, location=(445, 748), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.max_endurance, location=(508, 710), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.current_endurance, location=(1383, 510), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.heart_score, location=(842, 785), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.heart_tn, location=(778, 750), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.max_hope, location=(842, 710), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.wits_score, location=(1175, 785), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.wits_tn, location=(1112, 750), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.parry, location=(1175, 710), color='black', font=("Helvetica", 18), text_location=sg.TEXT_LOCATION_CENTER)
    draw_skills(active_character, window)
    window.maximize()
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event == "MouseWheel:Up":
            window['-GRAPH-'].move(0, -25)
        if event == "MouseWheel:Down":
            window['-GRAPH-'].move(0, 25)
        if event == "Up:38":
            window['-GRAPH-'].move(0, -25)
        if event == "Down:40":
            window['-GRAPH-'].move(0, 25)
        if event == "Left:37":
            window['-GRAPH-'].move(25, 0)
        if event == "Right:39":
            window['-GRAPH-'].move(-25, 0)

    window.close()







if __name__ == "__main__":
    main()