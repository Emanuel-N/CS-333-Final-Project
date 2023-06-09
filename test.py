import unittest 

from player import Player
from card import Card
from deck import Deck
from gofishgame import GoFishGame

class TestCard(unittest.TestCase):
    def test_card_instance(self): 
        card = Card("Diamonds", "5")
        self.assertEqual(str(card), "5 of Diamonds")

class TestDeck(unittest.TestCase):
    def test_deck_instance(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_shuffle(self): 
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle() 
        self.assertNotEqual(str(deck1.cards[0]),str(deck2.cards[0]) )

    def test_deck_deal_card(self): 
        deck = Deck() 
        self.assertEqual(str(deck.deal_card()), "King of Spades")

    def test_deal_empty_deck(self): 
        deck = Deck() 
        deck.cards = []
        self.assertEqual(deck.deal_card(), None)

class TestPlayer(unittest.TestCase): 
    def test_player_add_card_method(self): 
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        self.assertEqual(str(player.hand[0]), "5 of Diamonds")

    def test_player_remove_card_method(self): 
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        player.remove_card(card)
        self.assertEqual(len(player.hand), 0)

    def test_player_rank_card_equal(self): 
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        self.assertEqual(player.has_rank("5"), True)

    def test_player_rank_card_not_equal(self): 
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        self.assertEqual(player.has_rank("3"), False)

    def test_player_rank_count(self): 
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        self.assertEqual(player.get_rank_count("5"), 1)

    def test_player_set_count(self): 
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        card = Card("Hearts", "5")
        player.add_card(card)
        card = Card("Clubs", "5")
        player.add_card(card)
        card = Card("Spades", "5")
        player.add_card(card)
        self.assertEqual(str(player.get_books()), str(["5"]))

class TestGoFishGame(unittest.TestCase): 
    def test_go_fish_game_player_count(self): 
        game = GoFishGame(3)
        self.assertEqual(len(game.players), 3)
    
    def test_go_fish_game_next_player(self):
        game = GoFishGame(2)
        initial_player = game.get_current_player()
        game.next_player()
        next_player = game.get_current_player()
        self.assertNotEqual(str(initial_player), str(next_player))

class TestIntergration(unittest.TestCase): 
    def test_card_and_deck_relationship(self):
        card = Card("Hearts", "Ace")
        deck = Deck() 
        self.assertEqual(str(deck.cards[0]), str(card))

    def test_card_and_player_relationship(self):
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        card = Card("Hearts", "5")
        player.add_card(card)
        card = Card("Clubs", "5")
        player.add_card(card)
        card = Card("Spades", "5")
        player.add_card(card)
        self.assertEqual(str(player.get_books()), str(list(card.rank)))
    
    def test_player_and_gofishgame_relationship(self):
        game = GoFishGame(2)
        player = Player("player")
        card = Card("Diamonds", "5")
        player.add_card(card)
        card = Card("Hearts", "5")
        player.add_card(card)
        card = Card("Clubs", "5")
        player.add_card(card)
        card = Card("Spades", "5")
        player.add_card(card)
        card = Card("Spades", "6")
        player.add_card(card)
        game.deal_cards_to_players()
        self.assertEqual(len(game.players[0].hand), len(player.hand))

    def test_deck_and_gofishgame_relationship(self):
        game = GoFishGame(2)
        deck = Deck() 
        self.assertEqual(len(game.deck.cards), len(deck.cards))

    def test_card_and_gofishgame_relationship(self): 
        game = GoFishGame(2)
        card = Card("Spades", "6")
        game.players[0].add_card(card)

        self.assertEqual(str(game.players[0].hand[0]), str(card))

# testing
if __name__ == '__main__': 
    unittest.main()