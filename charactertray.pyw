# @todo
# add copymode functionality

import os
import time
import json
from pystray import Icon, Menu, MenuItem as Item
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
    with open('characters.json', 'r') as f:
        json_data = json.load(f)
    return json_data

# All low-level menu Items must have:
#   text: a string beginning with the character that will be typed when they are clicked (example: '— (em dash)')
#   action: on_clicked
# All submenu menu Items must have:
#   text: any string as its name
#   arg2: a submenu of only items.

def SubmenuItem(name, contents): # returns an Item called 'name' consisting of a submenu containing (contents)
    return Item(name, Menu(*(Item(i, on_clicked) for i in contents)))
def SubmenuItemsTuple(contents):
    return tuple(Item(i, on_clicked) for i in contents)

dashesTuple = ('- (hyphen)',
               '– (en dash)',
               '— (em dash)',
               '⸺ (2-em dash)',
               '⸻ (3-em dash)',
               '− (minus sign)')
#submenuMenuItems  = (SubmenuItem('dashes', dashesTuple),)
#submenuMenuItems += (SubmenuItem('Spanish uppercase', 'ÁÉÍÓÚÜÑ'),)
#submenuMenuItems += (SubmenuItem('Spanish lowercase', 'áéíóúüñ'),)
#submenuMenuItems += (SubmenuItem('Greek uppercase', 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'),)
#submenuMenuItems += (SubmenuItem('Greek lowercase', 'αβγδεζηθικλμνξοπρστυφχψω'),)
#submenuMenuItems += (SubmenuItem('math', 'π°−×÷⁰¹²³⁴≠≤≥⟨⟩∂'),)
#submenuMenuItems += (SubmenuItem('emoji', '👍'),) # does not work because Keyboard.type('👍') is not supported

submenuMenuItems  = (Item('dashes', Menu(*SubmenuItemsTuple(dashesTuple))),)
submenuMenuItems += (Item('Spanish uppercase', Menu(*SubmenuItemsTuple('ÁÉÍÓÚÜÑ'))),)
submenuMenuItems += (Item('Spanish lowercase', Menu(*SubmenuItemsTuple('áéíóúüñ'))),)
submenuMenuItems += (Item('Greek uppercase', Menu(*SubmenuItemsTuple('ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'))),)
submenuMenuItems += (Item('Greek lowercase', Menu(*SubmenuItemsTuple('αβγδεζηθικλμνξοπρστυφχψω'))),)
submenuMenuItems += (Item('math', Menu(*SubmenuItemsTuple('π°−×÷⁰¹²³⁴≈≠≤≥⟨⟩∂'))),)


#favoritesTuple = (*'αβηθλμπρσωඞ¢€£¥áéíóúüñ', '— (em dash)')
#favoritesMenuItems = tuple(Item(character, on_clicked) for character in favoritesTuple)

favoritesMenuItems = SubmenuItemsTuple((*'αβηθλμπρσωඞ¢€£¥áéíóúüñş', '— (em dash)'))

iconpath = os.path.join(os.path.dirname(__file__), 'enye.png')
icon = Icon('aengus_character_tray_icon', Image.open(iconpath), 'Aengus Character Tray')
icon.menu = Menu(Item("quit", icon.stop, default = False), *submenuMenuItems, *favoritesMenuItems)

if __name__ == '__main__':
    icon.run()
