import PySimpleGUI as sg
import time


from ui_functions import show_attribute, load_character


active_character = load_character("Arathorn")
x, y = sg.Window.get_screen_size()

layout = [
    [sg.Graph(canvas_size=(1920, 1080), background_color="black", graph_bottom_left=(0, 0), graph_top_right=(1920, 1080), expand_x=True, expand_y=True, change_submits=True, drag_submits=True, key='-GRAPH-')]
]

window = sg.Window("Character Sheet", layout, return_keyboard_events=True, finalize=True, resizable=True, element_justification='c', margins=(0, 0), element_padding=(0,0))
window['-GRAPH-'].draw_image(r"TOR_Elf_Character_Sheet_fillable (1).png", location=(0, 1080))
window['-GRAPH-'].draw_text(active_character.name, location=(970, 1000), color='black', font=("Helvetica", 22), text_location=sg.TEXT_LOCATION_CENTER)
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
