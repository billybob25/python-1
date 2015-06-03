''' this is my colors'''

green = '\033[0;32m'
cyan = '\033[0;32m'
blue = '\033[0;34m'
violet = '\033[1;35m'
orange = '\033[1;31m'
red = '\033[0;31m'
yellow ='\033[0;33m'
magenta = '\033[0;35m'
base02 = '\033[0;30m'
base01 = '\033[1;32m'
base00 = '\033[1;33m'
base0 = '\033[1;34m'
base1 = '\033[1;36m'
base2 = '\033[0;37m'
base3 = '\033[1;37m'
reset = '\033[0m'
clear = '\033[H\033[2J'

import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan, green])

if __name__ == '__main__':
    print(clear)
    print(orange + "Orange" + reset)
    print(red + "red" + reset)
    print(yellow + "yellow" + reset)
    print(magenta + "magenta" + reset)
    print(base02 + "base02" + reset)
    print(base01 + "base01" + reset)
    print(base00 + "base00" + reset)
    print(base1 + "base1" + reset)
    print(base2 + "base2" + reset)
    print(base3 + "base3" + reset)
    print(reset + "reset" + reset)
    print(clear + "clear" + reset)
