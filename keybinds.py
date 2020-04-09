import keyboard 
from auto import safe_click_all_buildings, safe_click, buyall_pos
keyboard.add_hotkey('g', lambda: safe_click_all_buildings()  )
keyboard.add_hotkey('f', lambda: safe_click(*buyall_pos)         )

keyboard.wait()