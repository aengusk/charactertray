# @DONE add json parse functionality
# @TODO add copymode functionality
# @TODO add argparse functionality and installation

import os
import time
import json
from pystray import Icon, Menu, MenuItem
from PIL import Image
from pynput.keyboard import Key, Controller
import pyperclip

typemode = True
Keyboard = Controller()

def switchWindow():
    Keyboard.press(Key.alt)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.release(Key.alt)

def on_clicked(icon, item):
    #print(item)
    if typemode:
        switchWindow()
        time.sleep(0.3)
        Keyboard.type(str(item)[0])
    else:
        pyperclip.copy(str(item)[0])

def parse_json():
    '''
    IN PROGRESS
    parses characters.json in the same directory level as charactertray.pyw
    and returns a tuple of MenuItems
    to be unpacked by icon.menu = Menu(*tuple)
    '''
    with open('characters.json', 'r', encoding='utf-8') as f:
        all_submenu_data = json.load(f)
    all_menu_items = []
    for submenu_title in all_submenu_data.keys():
        submenu_contents = all_submenu_data[submenu_title]
        # submenu_contents may be a string, as in 'αβγδεζηθικλμνξοπρστυφχψω',
        # or it may be a list (when characters are annotated), as in ['- (hyphen)', '– (en dash)', '— (em dash)']

        if submenu_title == 'favorites':
            # favorites get appended to all_menu_items as individual MenuItems at the top level
            all_menu_items.extend(MenuItem(character, on_clicked) for character in submenu_contents)
        else:
            # non-favorites get appended to all_menu_items grouped together into a submenu
            submenu = Menu(*(MenuItem(character, on_clicked) for character in submenu_contents))
            all_menu_items.append(MenuItem(submenu_title, submenu))
    return all_menu_items

all_menu_items = parse_json()

iconpath = os.path.join(os.path.dirname(__file__), 'enye.png')
icon = Icon('aengus_character_tray_icon', Image.open(iconpath), 'Aengus Character Tray')
icon.menu = Menu(MenuItem("quit", icon.stop, default = False), *all_menu_items)

if __name__ == '__main__':
    icon.run()
