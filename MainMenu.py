from pynput import keyboard
from os import system, name

#here is some stuff as a test on github

CurrentLine = 1
MaxLines = 6

MenuLines = "line 1" , "line 2" , "line 3" , "line 4" , "line 5" , "line 6"

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

    if str(currentKey) == "Key.up" and CurrentLine > 1:
        CurrentLine  -= 1
        #print(CurrentLine)

    DrawMenu(CurrentLine, MaxLines)


def DrawMenu(CurrentLine, Maxlines):
    #print("\n" * 100)
    system('cls')
    OneLessThanCurrentLine = CurrentLine - 1
    TheRest = MaxLines - CurrentLine

    for i in range(OneLessThanCurrentLine):
        print("line")
    print("[line]")
    print("line \n" * TheRest)


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


