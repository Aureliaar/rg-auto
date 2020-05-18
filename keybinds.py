import keyboard 
from auto import safe_click_all_buildings, safe_click, buyall_pos, load_research_template, safe, menu, buyall_merc_pos
from auto import research_template_pos, confirm_template, exca_pos
keyboard.add_hotkey('g', lambda: safe_click_all_buildings()  )
keyboard.add_hotkey('f', lambda: safe_click(*buyall_pos)         )

keyboard.add_hotkey('a', lambda: safe(menu, 1)         )
keyboard.add_hotkey('s', lambda: safe(menu, 2)         )
keyboard.add_hotkey('d', lambda: safe(menu, 3)         )
keyboard.add_hotkey('z', lambda: safe_click(*research_template_pos)        )

keyboard.add_hotkey('x', lambda: safe_click(*exca_pos)         )


keyboard.add_hotkey('q', lambda: safe(load_research_template, 1)         )
keyboard.add_hotkey('w', lambda: safe(load_research_template, 2)         )
keyboard.add_hotkey('e', lambda: safe(load_research_template, 3)         )
keyboard.add_hotkey('r', lambda: safe(load_research_template, 4)         )
keyboard.add_hotkey('t', lambda: safe(load_research_template, 5)         )
keyboard.add_hotkey('y', lambda: safe(load_research_template, 6)         )

keyboard.add_hotkey('v', lambda: safe_click(*buyall_merc_pos)         )



keyboard.wait()