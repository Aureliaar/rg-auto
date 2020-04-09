
import win32gui
import win32api
import win32con
import time
import random
import math

window_name = "Realm Grinder"
y_offset = 32
#positions
#menus
buyall_pos = (285, 85)
buyall_merc_pos = (215, 85)
abdicate_pos = (220, 56)
confirm_abdicate_pos = (774, 828)
exca_pos = (180, 86)
template_pos=(853, 600)
template_1st_pos=(821, 720)
import_pos=(880, 950)
buy_third = (241, 177) #bloodline after all other buys
titan_bloodline = (780, 759)

close_merc_menu_pos =(1070, 70)

global_wait_mult=1
DEBUG_CLICKS=False

tricaster_template = "GB1,UD2,UD5,UD7,DM3,TT6,DD5,DD6,DD7,DD9,DN3,DW8,SP:Grand Balance,SP:Fairy Chanting"

def wfocused():
    focused = win32gui.GetForegroundWindow()
    app = win32gui.FindWindow(None, window_name)
    #print("{}, {}, {}".format(focused, app, focused==app))
    return focused == app

#buildings
def building(index):
    return (1600, 340+60*index)

def spell(index):
    click(1400, 450+50*index)

def menu(index):
    return (42, 413+75*index)

def click(x, y, wait=33):
    hWnd = win32gui.FindWindow(None, window_name)
    lParam = win32api.MAKELONG(x, y-y_offset)
    if DEBUG_CLICKS:
        print("{},{}".format(x,y))

    win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
    time.sleep(global_wait_mult * wait/1000)

def safe_click(x, y, wait=33):
    if not wfocused():  return
    click(x, y, wait)

def click_all_buildings():
    indexes = list(range(1, 12))
    random.shuffle(indexes)
    for i in indexes:
        click(*building(i))

def safe_click_all_buildings():
    if not wfocused():  return
    click_all_buildings()

def abdicate(safe=True, need_confirm=False):
    if safe: 
        click(*menu(2), wait=500)
        click(*menu(1), wait=500)
    click(*abdicate_pos, wait=500)
    if not need_confirm:
        click(*confirm_abdicate_pos, wait=500)

def exca(wait=250):
    click(*menu(1), wait=250)
    click(*menu(2), wait=250)
    click(*exca_pos, wait=250)
    click(*menu(1), wait=250)


def buy_all(merc=False):
    if merc:
        click(*buyall_merc_pos, wait=250)
        return
    click(*buyall_pos, wait=250)

def buy(index, wait=33):
    index = index-1
    click(120+60*(index%7), 180+60*math.floor(index/7), wait)

def load_template(template):
    click(*buyall_pos, wait=500)
    click(*template_pos, wait=250)
    click(*template_1st_pos, wait=250)
    click(*import_pos, wait=500)

def merc_load_template():
    buy_all(merc=True)
    exca()
    spell(1)
    load_template(tricaster_template)
    time.sleep(2)

def tricaster():
    abdicate()
    buy_all()
    buy(4) #become evil
    click_all_buildings()
    buy_all()
    click_all_buildings()
    buy_all()
    time.sleep(0.5)
    buy(9, wait=0) #become merc if there's some fucking gem idiocy abound
    buy(8, wait=250) #become merc 
    click(*close_merc_menu_pos, wait=33)

    spell(2)
    #Template safe buy
    for i in range(1, 4):
        merc_load_template()


    #Bloodline
    buy(6)
    time.sleep(0.5)
    click(*titan_bloodline)
    buy_all(merc=True)

    time.sleep(25)
    spell(5)
    time.sleep(4)
    spell(6)
    spell(2)
    time.sleep(10)
    spell(4)

    for i in range(100):
        spell(1)
        time.sleep(0.1)
        if not i%10:
            click_all_buildings()
            buy_all(merc=True)



def multi_tricaster(n):
    for i in range(1, n):
        tricaster()
        print(i)


def multi_spell(n, index, first_buy=7, second_buy=5):
    for i in range(1, n):
        cast_spell(index, first_buy, second_buy)
        print(i)

def cast_spell(index, first_buy=7, second_buy=5):
    abdicate()
    buy(first_buy)
    buy(second_buy) 
    time.sleep(0.5)
    spell(index)
    time.sleep(0.5)
