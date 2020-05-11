
import win32gui
import win32api
import win32con
import time
import random
import math

from positions import *


window_name = "Realm Grinder"

global_wait_mult=1
DEBUG_CLICKS=False


def wfocused():
    focused = win32gui.GetForegroundWindow()
    app = win32gui.FindWindow(None, window_name)
    #print("{}, {}, {}".format(focused, app, focused==app))
    return focused == app

#buildings
def building(index):
    return (farm_click[0], farm_click[1]+60*(index-1))

def spell(index, ctrl=False):
    click(tc_click[0], tc_click[1]+50*(index-1), ctrl=ctrl)


def menu(index, wait=100):
    click(up_click[0], up_click[1]+75*(index-1), wait)

def confirm_template(index):
    click(confirm_template_click[0], confirm_template_click[1]+20*(index-1))
    click(*import_pos, wait=100)


def click(x, y, wait=33, ctrl=False):
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
        menu(2, wait=500)
        menu(1, wait=500)
    click(*abdicate_pos, wait=500)
    if not need_confirm:
        click(*confirm_abdicate_pos, wait=500)

def exca(wait=250):
    menu(1, wait=250)
    menu(2, wait=250)
    click(*exca_pos, wait=250)
    menu(1, wait=250)


def buy_all(merc=False):
    if merc:
        click(*buyall_merc_pos, wait=250)
        return
    click(*buyall_pos, wait=250)

def buy(index, wait=33):
    index = index-1
    click(120+60*(index%7), 180+60*math.floor(index/7), wait)

def load_merc_template():
    click(*buyall_pos, wait=500)
    click(*template_pos, wait=250)
    click(*template_1st_pos, wait=250)
    click(*import_pos, wait=500)

def mercExcaAndLoad():
    buy_all(merc=True)
    exca()
    spell(1)
    load_merc_template()
    time.sleep(2)

def safe(func, *args, **kwargs):
    if not wfocused(): return 
    func(*args, **kwargs)

def load_research_template(index):
    click(*research_template_pos, wait=250)
    confirm_template(index)


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
        mercExcaAndLoad()


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

def multi(n, delay, abdicate_when_done, func, *args, **kwargs):
    for i in range(0, n):
        func(*args, **kwargs)
        print(i)
        time.sleep(delay/1000)
    if abdicate_when_done:
        abdicate()

def dwangel():
    abdicate()
    buy(5) #good
    buy(10) #angel
    buy_all()
    click_all_buildings()
    #Bloodline
    buy(21)
    time.sleep(0.5)
    click(*druid_bloodline)

    exca()
    buy_all()
    time.sleep(0.2)
    buy(6) #dwarf
    buy_all()


def dwangel_spells():
    spell(2)
    spell(3)
    spell(4)
    spell(5)
    spell(6) 
    for i in range(1, 100):
        click(1)

def reset_spell(index):
    hWnd = win32gui.FindWindow(None, window_name)

    win32api.SendMessage(hWnd, win32con.WM_KEYDOWN, ord('r'), 0)
    spell(index)
    win32api.SendMessage(hWnd, win32con.WM_KEYUP, ord('r'), 0)

brainwave_cancel_pos = (1128, 815)