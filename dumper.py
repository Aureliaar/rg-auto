from pynput.mouse import Listener


def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    if pressed:
        print("{}, {}".format(x, y))

def on_scroll(x, y, dx, dy):
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
