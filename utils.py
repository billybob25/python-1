"""This my awsome utility kitchen sink. Don't judge me."""

import colors as c

def ask(question):
    print(question)
    answer = input("> ")
    return answer


if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?")
    



