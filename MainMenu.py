from pynput import keyboard
from os import system

CurrentLine = 0

MenuLines = "line 0", "line 1", "line 2", "line 3", "line 4", "line 5", "line 6"

MaxLine = len(MenuLines) - 1
NoOfLines = len(MenuLines)


def on_press(key):
    current_key = key
    move_selector(current_key)


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def move_selector(current_key):
    global CurrentLine
    global MaxLine
    if str(current_key) == "Key.down" and CurrentLine < MaxLine:
        CurrentLine += 1

    if str(current_key) == "Key.up" and CurrentLine > 0:
        CurrentLine -= 1

    draw_menu()


def draw_menu():
    print("\n" * 10)
    system('cls')

    for i in range(NoOfLines):
        if CurrentLine == i:
            print("[", MenuLines[i], "]")
        else:
            print(MenuLines[i])


draw_menu()


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
