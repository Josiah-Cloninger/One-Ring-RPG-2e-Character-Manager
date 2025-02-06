import PySimpleGUI as sg
import PIL
from PIL import Image

from ui_functions import load_character
from show_character_gui import draw_all

def main():
    size = (1920, 1080)
    layout = [
        [sg.Graph(size, (0, 0), size, background_color="black",  expand_x=True, expand_y=True, pad=(0, 0), key='-GRAPH-')]
    ]

    window = sg.Window('Window Title', layout, resizable=True, return_keyboard_events=True, finalize=True)
    active_character = load_character("Arathorn")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            break
        # window.size = (window.size[0] + 10, window.size[1] + 10)'
        window['-GRAPH-'].erase()
        img = Image.open(r"TOR_Elf_Character_Sheet_fillable (1).png")
        img = img.resize(window.size)
        img.save(r"TOR_Elf_Character_Sheet_fillable (2).png")
        window['-GRAPH-'].draw_image(r"TOR_Elf_Character_Sheet_fillable (2).png", location=(0, 1080))
        window['-GRAPH-'].CanvasSize = window.size
        draw_all(active_character, window)

    window.close()

if __name__ == '__main__':
    main()