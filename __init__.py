from random import randint
from time import sleep
from sys import stdout
import keyboard

def answer():
    return input("> ").lower()[0]

def printf(speaker:str, string:str):
    print("[" + speaker.upper() + "] ", end="")
    for char in string:
        print(char, end="")
        stdout.flush() 
        sleep(0.02)
        if keyboard.is_pressed('x'):
            sleep(0.2
            )
            break
    print("")

def chapter0_2():
    printf("llama", "Attack the human!")
    printf("narrator", "A bunch of llamas charge at you, however, one alpaca stands in front of them, a minigun mounted to it's back whirring up.")

def chapter0_1():
    printf("narrator", "You awake inside your house. You hear gunshots outside of your house. Curious as to what is happening, you go outside.")
    printf("narrator", "You see alpacas and llamas fitted with some sort of makeshift armor and weaponry.")
    printf("system", "Will you:\n 1) Join the fight\n 2) Go back inside")
    choice = answer()
    if (choice == "1" or choice == "j"):
        printf("narrator", "You go inside your house and find your Rusty Revolver. (5 DMG)")
        printf("system", "Item added to your inventory! (Rusty Revolver)")
        chapter0_2()
    elif (choice == "2" or choice == "g"):
        printf("narrator", "You go back inside your house and are immediately slaughtered.")
        printf("system", "Respawning in 3... 2... 1...") 
        chapter0()

def chapter0():
    chapter0_1()
    
if (__name__ == "__main__"):
    tips = [
        "Pressing 'X' during dialog skips it!",
        "You can type the number of your choice or the choice itself.",
        "It's always possible to leave combat without killing someone.",
        "Every choice you make impacts your KARMA.",
        "Master Alpaca knows everything about you... and deleting your save won't change that fact."
    ]

    tip = randint(0, len(tips) - 1)
    printf("tip", tips[tip])
    chapter0()