'''
# Class for the two player card game war
'''

import random
import time
import war.player as player

class War:
    def __init__(self, verbose_output=False):
        self.player_1 = player.Player('player_1', [])
        self.player_2 = player.Player('player_2', [])
        self.result = None
        self.verbose_output = verbose_output

        self._allot_cards()

    def _allot_cards(self):
        '''
        Order of card, high to low:
            Ace: 14, King: 13, Queen: 12, Jack: 11, 10-2
        '''
        cards = list(range(2,15))*4
        random.seed(time.time())
        random.shuffle(cards)

        self.player_1.add_cards(cards[:len(cards)//2])
        self.player_2.add_cards(cards[len(cards)//2:])

    def run(self):
        '''
        RULES:
            # Game terminates when one of the player runs out of cards
            # Tie occurs when both the players are left with 1 card in a war
        '''
        while len(self.player_1) and len(self.player_2):
            card_1, card_2 = self.player_1.play(), self.player_2.play()
            if self.verbose_output:
                print("cards played:", card_1, card_2)

            if card_1 > card_2:
                self.player_1.add_cards([card_1, card_2])
            elif card_1 < card_2:
                '''
                The order of cards being added is reversed to avoid exchaging
                of cards deck when players win alternatively: scenario explained
                in detail in the documentation
                '''
                self.player_2.add_cards([card_2, card_1])
            else:
                self._war([card_1, card_2])

                # If the game ended during the war then return the result
                if self._game_ended():
                    return self.result

            if self.verbose_output:
                print("player_1: {} player_2: {}".format(len(self.player_1),
                                len(self.player_2)))

        # Case where one of the players ran out of cards
        self._set_winner()
        return self.result

    def _war(self, cards):
        while cards[-1] == cards[-2] and len(self.player_1) > 1 and len(self.player_2) > 1:
            # cards placed face-down
            cards += [self.player_1.play(), self.player_2.play()]
            # cards placed face-up
            cards += [self.player_1.play(), self.player_2.play()]

        if cards[-2] > cards[-1]:
            self.player_1.add_cards(cards)
        elif cards[-1] > cards[-2]:
            self.player_2.add_cards(cards)
        else:
            # At least one player has onlyone card left and we need break the tie
            self._break_tie()

    def _break_tie(self):
        if len(self.player_1) == 1 and len(self.player_2) == 1:
            # Reached a tie
            self._set_result("It's a tie!")
        elif len(self.player_1) > 1:
            self._set_winner(self.player_1)
        else:
            self._set_winner(self.player_2)

    def _set_result(self, result):
        self.result = result

    def _set_winner(self, player=None):
        '''
        If player == None:
            Case where one of the players ran out of cards, set the winner
        If player is given just set their status and set result
        '''
        if not player:
            if len(self.player_1):
                player = self.player_1
            elif len(self.player_2):
                player = self.player_2

        player.set_status(True)
        self._set_result("{} won!!".format(player.name))

    def _game_ended(self):
        if self.result:
            return True

        return False
