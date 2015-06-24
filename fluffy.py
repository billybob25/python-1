"""The pink fluffy unicorn quiz questions module"""

import colors as c
from utils import ask

intro = c.clear + c.magenta + '''
Welcome to the Fluffy Unicorn Quiz.

let's test your knowlegde...'''

def q1():
    answer = ask("What are the colors are the unicorns?")
    if answer == 'pink':
        return True
    return False

def q2():
    answer = ask("What are the unicorns dancing on?")
    if answer == 'rainbow':
        return True
    return False

def q3():         
    answer = ask("Use one word that would describe the unicorns magical fur?")
    if answer.startswith("smile"):
        print(":)")
        return True
    print(":<")
    return False

question = [q1,q2,q3]
