from game.player import Player
import unittest

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player('player', list(range(2,15))*4)

    def test_len(self):
        self.assertEqual(len(self.player), 52)

    def test_play(self):
        self.assertEqual(self.player.play(), 14)

    def test_add_cards(self):
        self.player.add_cards([33,34])
        self.assertEqual(len(self.player), 54)
        self.assertEqual(self.player.cards[:2], [33,34])

    def test_set_status(self):
        self.assertFalse(self.player.won)
        self.player.set_status(True)
        self.assertTrue(self.player.won)

    def test_is_winner(self):
        self.assertFalse(self.player.is_winner())
        self.player.set_status(True)
        self.assertTrue(self.player.is_winner())
