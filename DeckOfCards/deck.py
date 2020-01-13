# import random
# class Card:
#     def __init__(self, type, number):
#         self.type = type
#         self.number = number
#
# class Deck:
#     cards = {}
#     def __init__(self):
#         self.cards = {i+1:[Card("Red", i+1), Card("Blue", i+1), Card("Green", i+1), Card("Yellow", i+1)]
#                       for i in range(0,10)}
#     def shuffle(self):
#         keys = list(self.cards.keys())
#         random.shuffle(keys)
#         shuffledDic = dict()
#         for key in keys:
#             shuffledDic.update({key : self.cards[key]})
#         self.cards = shuffledDic
#
#     def deal(self):
#         pass
#
#     def __iter__(self):
#         pass

import random
class Card:
    def __init__(self, type, number):
        self.type = type
        self.number = number

class Deck:
    cards = []
    def __init__(self):
        self.cards = [Card("Red", i+1) for i in range(0,10)] +\
                     [Card("Yellow", i+1) for i in range(0,10)]+ \
                     [Card("Green", i + 1) for i in range(0, 10)]+ \
                     [Card("Blue", i + 1) for i in range(0, 10)]
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            raise StopIteration

deck = Deck()
deck.shuffle()
for item in deck:
    print(f"{item.type}, {item.number}")

print()

if deck.cards:
    card = deck.deal()
else:
    print( "the deck is empty" )