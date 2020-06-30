from pynput import keyboard
from os import system

CurrentLine = 0

FirstMenu = "line 0", "line 1", "line 2", "line 3", "line 4", "line 5", "line 6"
SecondMenu = "line 7", "line 8", "line 9", "line 10", "line 11", "line 12", "line 13"
CurrentMenu = SecondMenu

MaxLine = len(CurrentMenu) - 1
NoOfLines = len(CurrentMenu)


def on_press(key):
    current_key = key
    if str(current_key) == "Key.down" or str(current_key)== "Key.up":
        move_selector(current_key)
    elif str(current_key) == "Key.enter":
        select_line()


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


def select_line():
    global CurrentMenu
    print("current line is ", CurrentLine, "and line name is ", CurrentMenu[CurrentLine])
    if CurrentMenu[CurrentLine] == "line 7":
        CurrentMenu = FirstMenu
        print("it is now the first menu")
        draw_menu()


def draw_menu():
    print("\n" * 10)
    system('cls')

    for i in range(NoOfLines):
        if CurrentLine == i:
            print("[", CurrentMenu[i], "]")

        else:
            print(CurrentMenu[i])


draw_menu()


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
