import pyautogui
import keyboard

print()
print("Py Auto Clicker by J1D1:")
print()
print("This program was only tested on Windows, it may not work on other systems.")
print()

startleftauto = input("Enter a key to start left auto clicker: ")
startrightauto = input("Enter a key to start right auto clicker: ")
stopauto = input("Enter a key to stop all auto clickers: ")
print(f"You might need to press \"{stopauto}\" multiple times")
print("Ctrl + C to exit the program (an error may appear, just ignore it)")
print("Running...")

def leftautofunc():
    while True:
        pyautogui.click()
        if keyboard.is_pressed(stopauto):
            break
def rightautofunc():
    while True:
        pyautogui.rightClick()
        if keyboard.is_pressed(stopauto):
            break

while True:
    if keyboard.is_pressed(startleftauto):
        leftautofunc()
    if keyboard.is_pressed(startrightauto):
        rightautofunc()