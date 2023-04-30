import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(suit, rank)
                self.cards.append(card)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_card(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()