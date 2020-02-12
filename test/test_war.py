import unittest
from war.war import War

class WarTestCase(unittest.TestCase):
    def setUp(self):
        self.war = War()

    def test_init(self):
        self.assertIsNone(self.war.result)
        self.assertFalse(self.war.verbose_output)

        self.assertEqual(self.war.player_1.name, 'player_1')
        self.assertEqual(self.war.player_2.name, 'player_2')
        self.assertEqual(len(self.war.player_1), 26)
        self.assertEqual(len(self.war.player_2), 26)

        self.war = War(verbose_output=True)
        self.assertTrue(self.war.verbose_output)

    def test_run_general(self):
        result = self.war.run()
        self.assertIn(result, ["It's a tie!", "player_1 won!!", "player_2 won!!"])

        if result == "It's a tie!":
            self.assertEqual(len(self.war.player_1), 1)
            self.assertEqual(len(self.war.player_2), 1)
        elif result == "player_1 won!!":
            self.assertTrue(len(self.war.player_1) > 1)
            self.assertTrue(len(self.war.player_2) <= 1)
        elif result == "player_2 won!!":
            self.assertTrue(len(self.war.player_1) <= 1)
            self.assertTrue(len(self.war.player_2) > 1)

    def test_run_tie(self):
        self.war.player_1.cards = list(range(2,15))*2
        self.war.player_2.cards = list(range(2,15))*2

        result = self.war.run()
        self.assertEqual(result, "It's a tie!")
        self.assertEqual(len(self.war.player_1), 1)
        self.assertEqual(len(self.war.player_2), 1)

    def test_run_player_1_win(self):
        self.war.player_1.cards = list(range(2,15))*2
        self.war.player_1.cards.sort()
        self.war.player_2.cards = list(range(2,15))*2
        self.war.player_2.cards.sort(reverse=True)

        result = self.war.run()
        self.assertEqual(result, "player_1 won!!")
        self.assertEqual(len(self.war.player_1), 52)
        self.assertEqual(len(self.war.player_2), 0)

    def test_run_player_2_win(self):
        self.war.player_1.cards = list(range(2,15))*2
        self.war.player_1.cards.sort(reverse=True)
        self.war.player_2.cards = list(range(2,15))*2
        self.war.player_2.cards.sort()

        result = self.war.run()
        self.assertEqual(result, "player_2 won!!")
        self.assertEqual(len(self.war.player_1), 0)
        self.assertEqual(len(self.war.player_2), 46)
