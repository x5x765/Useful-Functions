from random import randint
from time import sleep
def delayed_print(string, delay = 200, random = True, randomness = 150):
    charList = list(string)
    newDelay = 0
    for char in charList:
        print(char, end="")
        if random:
            newDelay = randint(delay-randomness, delay+randomness)
        sleep(newDelay/1000)

delayed_print(input())
