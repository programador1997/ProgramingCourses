import random
"""
import all the funtions of the random py
import random

import only the funtions choise 
from random iport choice

"""

def main():
    shufflecards()

def coinToss():
    coin = random.choice(["heads", "tails"])
    print(coin)

def randomnumber(a,b):
    number = random.randint(a,b)
    print(number)

def shufflecards():
    cards = ["joto", "quina", "rey"]
    random.shuffle(cards)
    for card in cards:
        print(card)

main()