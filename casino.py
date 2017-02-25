import random

class Greeter(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)

    def goodbye(self):
        print("Goodbye " + self.name)

class Die(object):
    def __init__(self, sides):
         self.sides = sides

    def roll(self):
         return random.randint(1,self.sides)

class Deck(object):
    def shuffle(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(suit  + " of " + rank)
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()  
    