import PySimpleGUI as sg
import time


from ui_functions import show_attribute, load_character


def focus(window):
    return window.TKroot.focus_displayof() is not None


def check_focus(window, window_background, widget):
    # Some events for children of window passed
    if widget == window.TKroot:
        window_background.BringToFront()
        window.BringToFront()


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


    layout = [
        [sg.Graph(canvas_size=(1920, 1080), graph_bottom_left=(0, 0), graph_top_right=(1920, 1080), key='-GRAPH-'),],
        # [sg.draw_text(f"{active_character.name}", font=("Helvetica", 20), text_color='black')],
    ]
    return layout


def main():
    active_character = load_character("Lif")

    background_layout = [
        [sg.Col([[sg.T('_', enable_events=True, key='-MINIMIZE-'), sg.Text('❎', enable_events=True, key='Exit')]], element_justification='r', key='-C-', grab=True,
        pad=(0, 0))],
        [sg.Image(r"One Ring RPG Blank Character Sheet Close.png")]
]
    print(sg.Window.get_screen_size())
    window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0))
    window_background['-C-'].expand(True, False, False)  # expand the titlebar's rightmost column so that it resizes correctly

    layout = create_layout()

    window = sg.Window("Character Information", layout, finalize=True, transparent_color=sg.theme_background_color(), resizable=True, element_justification='c', margins=(0, 0), element_padding=(0,0))
    window['-GRAPH-'].draw_text(active_character.name, location=(960, 1040), color='black', font=("Helvetica", 20), text_location=sg.TEXT_LOCATION_CENTER)
    window['-GRAPH-'].draw_text(active_character.age, location=(630, 975), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.culture, location=(320, 975), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.calling, location=(280, 900), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.shadow_path, location=(675, 940), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window['-GRAPH-'].draw_text(active_character.patron, location=(675, 900), color='black', font=("Helvetica", 12), text_location=sg.TEXT_LOCATION_BOTTOM_LEFT)
    window.maximize()
    window.bind('<FocusIn>', 'FocusIn')
    window.bind('<FocusOut>', 'FocusOut')
    while True:

        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event in ('FocusIn', 'FocusOut'):
            widget = window.user_bind_event.widget
            check_focus(window, window_background, widget)









if __name__ == "__main__":
    main()