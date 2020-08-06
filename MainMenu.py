from pynput import keyboard
from os import system


FirstMenu = "line 0", "line 1", "line 2", "line 3", "line 4", "line 5", "line 6", "line 8"
SecondMenu = "line 7", "line 8", "line 9", "line 10", "line 11", "line 12", "line 13"

CurrentMenu = FirstMenu
CurrentLine = 0

MaxLine = len(CurrentMenu) - 1
NoOfLines = len(CurrentMenu)


# reset the amount of lines and the length of list
def reset_menu(CurrentMenu):
    global NoOfLines
    global MaxLine
    MaxLine = len(CurrentMenu) - 1
    NoOfLines = len(CurrentMenu)
    print("reset menu ", NoOfLines)



# get the current key being pressed
def on_press(key):
    current_key = key
    if str(current_key) == "Key.down" or str(current_key)== "Key.up":
        move_selector(current_key)
    elif str(current_key) == "Key.right":
        select_line()


# stop the program when esc is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# changing the current line
def move_selector(current_key):
    global CurrentLine
    global MaxLine
    if str(current_key) == "Key.down" and CurrentLine < MaxLine:
        CurrentLine += 1
    if str(current_key) == "Key.up" and CurrentLine > 0:
        CurrentLine -= 1

    draw_menu()


# what happens when you select a line
def select_line():
    global CurrentMenu
    print("current line is ", CurrentLine, "and line name is ", CurrentMenu[CurrentLine])

    # here is where the actions of selecting the line goes
    if CurrentMenu[CurrentLine] == "line 7":
        CurrentMenu = FirstMenu
        print("it is now the first menu")
        reset_menu(CurrentMenu)
        draw_menu()
    elif CurrentMenu[CurrentLine] == "line 0":
        CurrentMenu = SecondMenu
        print("it is now the second menu")
        reset_menu(CurrentMenu)
        draw_menu()


# draw the menu to the screen
def draw_menu():

    print("\n" * 10)

    #system('cls')

    for i in range(NoOfLines):
        if CurrentLine == i:
            print("[", CurrentMenu[i], "]")
        else:
            print(CurrentMenu[i])


reset_menu(CurrentMenu)
draw_menu()


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
