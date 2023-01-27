import win32gui
import time
window_name = "Realm Grinder"

while(True):
    the_window_hwnd = win32gui.FindWindow(None, window_name)  # hwnd of the specific window, it could be whatever you what
    left_top_x, left_top_y, *useless_position = win32gui.GetWindowRect(the_window_hwnd) # get the position of window you gave.
    print(left_top_y)
    mouse_pos_x, mouse_pos_y = win32gui.GetCursorPos()
    pos_in_window_x, pos_in_window_y = (mouse_pos_x - left_top_x), (mouse_pos_y - left_top_y)

    print(pos_in_window_x, pos_in_window_y)
    time.sleep(1)