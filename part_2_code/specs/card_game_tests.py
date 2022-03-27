import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('Spades', 1)
        self.card2 = Card('Hearts', 10)
        self.card3 = Card('Diamonds', 7)
        self.game = CardGame

    def test_check_for_ace(self):
        result = self.game.check_for_ace(self.card1)
        self.assertTrue(result)

    def test_highest_card(self):
        result = CardGame.highest_card(self.card2, self.card3)
        self.assertEqual(result, self.card2)

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        result = self.game.cards_total(cards)
        self.assertEqual("You have a total of 18", result)
