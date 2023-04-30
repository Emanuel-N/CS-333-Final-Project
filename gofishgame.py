from deck import Deck
from player import Player
from card import Card

class GoFishGame:
    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        for i in range(num_players):
            name = f"Player {i+1}"
            player = Player(name)
            self.players.append(player)
        self.current_player_index = 0
        
    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        
    def play(self):
        # Deal cards to players
        for i in range(5):
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)
                
        while True:
            current_player = self.get_current_player()
            
            # Print current player's hand
            print(f"\n{current_player.name}'s hand:")
            for card in current_player.hand:
                print(card)
                
            # Check if player has any books
            books = current_player.get_books()
            for book in books:
                print(f"{current_player.name} has a book of {book}s!")
                for player in self.players:
                    if player != current_player:
                        player.remove_card(Card("", book))
                        
            # Ask another player for a rank
            rank = input(f"{current_player.name}, what rank do you want to ask for? ")
            if not rank in Card.RANKS:
                print("Invalid rank!")
                continue
                
            player_index = int(input("Which player do you want to ask? (Enter a number): ")) - 1
            if player_index < 0 or player_index >= len(self.players) or player_index == self.current_player_index:
                print("Invalid player!")
               
            target_player = self.players[player_index]
            if not target_player.has_rank(rank):
                print(f"{target_player.name} doesn't have any {rank}s. Go Fish!")
                card = self.deck.deal_card()
                if card is None:
                    print("The deck is empty!")
                    break
                else:
                    current_player.add_card(card)
            else:
                print(f"{target_player.name} has {target_player.get_rank_count(rank)} {rank}s!")
                cards_to_move = [card for card in target_player.hand if card.rank == rank]
                for card in cards_to_move:
                    target_player.remove_card(card)
                    current_player.add_card(card)
                    
            # Check if any player has an empty hand
            for player in self.players:
                if len(player.hand) == 0:
                    print(f"\n{player.name} has an empty hand!")
                    books = player.get_books()
                    for book in books:
                        print(f"{player.name} had a book of {book}s!")
                    self.players.remove(player)
                    if len(self.players) == 1:
                        print(f"\n{self.players[0].name} has won the game!")
                        return
                    
            self.next_player()