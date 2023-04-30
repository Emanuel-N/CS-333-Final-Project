from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)
        
    def remove_card(self, card):
        self.hand.remove(card)
        
    def has_rank(self, rank):
        for card in self.hand:
            if card.rank == rank:
                return True
        return False
    
    def get_rank_count(self, rank):
        count = 0
        for card in self.hand:
            if card.rank == rank:
                count += 1
        return count
    
    def get_books(self):
        books = []
        for rank in Card.RANKS:
            count = self.get_rank_count(rank)
            if count == 4:
                books.append(rank)
        return books