"""The minecraft  quiz questions module"""

import colors as c
from utils import ask

intro = c.clear + c.magenta + '''
Welcome to the Minecraft Quiz.

let's test your knowledge...'''

def q1():
    answer = ask("What color is the grass?")
    if answer == 'green':
        return True
    return False

def q2():
    answer = ask("What is the mod with pokemon?")
    if answer == 'pixelmon':
        return True
    return False

def q3():         
    answer = ask("What is in the end?")
    if answer.startswith("enderd"):
        print(":)")
        return True
    print(":<")
    return False

def q4():
    answer = ask("Who created minecraft?")
    if answer == 'notch':
        return True
    return False

def q5():
    answer = ask("Who is the Enemy if the game?")
    if answer == 'Herobrine':
        return True
    return False










question = [q1,q2,q3,q4,q5]
