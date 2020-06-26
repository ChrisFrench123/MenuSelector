from pynput import keyboard
from os import system, name


CurrentLine = 0


MenuLines = "line 0" , "line 1" , "line 2" , "line 3" , "line 4" , "line 5", "line 6"

MaxLines = len(MenuLines) - 1

def on_press(key):
    #print(key, "pressed")
    currentKey = key
    MoveSelector(currentKey)

def on_release(key):
    #print(key , "released")
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def MoveSelector(currentKey):
    global CurrentLine
    global MaxLines
    if str(currentKey) == "Key.down" and CurrentLine < MaxLines:
        CurrentLine  += 1
        #print(CurrentLine)

    if str(currentKey) == "Key.up" and CurrentLine > 0:
        CurrentLine  -= 1
        #print(CurrentLine)

    DrawMenu(CurrentLine, MaxLines)


def DrawMenu(CurrentLine, Maxlines):
    print("\n" * 10)
    print(CurrentLine)
    system('cls')



    for i in range (len(MenuLines)):
        if CurrentLine == i:
            print("[", MenuLines[i], "]")
        else:
            print(MenuLines[i])


DrawMenu(CurrentLine, MaxLines)


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


end = input("hi")
