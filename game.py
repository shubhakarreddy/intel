import random
class Player:
    def __init__(self, cards):
        self.cards = cards
        self.won = False

    def __len__(self):
        return len(self.cards)

    def _play(self):
        return self.cards.pop()

    def _add_cards(self, cards):
        self.cards = cards + self.cards

class War:
    def __init__(self):
        self.player_1 = Player(None)
        self.player_2 = Player(None)

        self._allot_cards()

    def _allot_cards(self):
        cards = list(range(2,15))*4
        random.shuffle(cards)

        self.player_1.cards = cards[:len(cards)//2]
        self.player_2.cards = cards[len(cards)//2:]

    def run_game(self):
        while len(self.player_1) and len(self.player_2):
            card_1, card_2 = self.player_1._play(), self.player_2._play()
            print("cards played:", card_1, card_2)
            if card_1 > card_2:
                self.player_1._add_cards([card_1, card_2])
            elif card_1 < card_2:
                self.player_2._add_cards([card_2, card_1])
            else:
                self._war([card_1, card_2])

                if self.player_1.won and self.player_2.won:
                    return "It's a draw!"
                elif self.player_1.won:
                    return "player_1 won!"
                elif self.player_2.won:
                    return "player_2 won!"

            print("player_1: {} player_2: {}".format(len(self.player_1), len(self.player_2)))

        if len(self.player_1):
            return "player_1 won!"
        elif len(self.player_2):
            return "player_2 won!"

    def _war(self, cards):
        while cards[-1] == cards[-2] and len(self.player_1) > 1 and len(self.player_2) > 1:
            cards += [self.player_1._play(), self.player_2._play()]
            cards += [self.player_1._play(), self.player_2._play()]

        if cards[-2] > cards[-1]:
            self.player_1._add_cards(cards)
        elif cards[-1] > cards[-2]:
            self.player_2._add_cards(cards)
        elif len(self.player_1) == 1 and len(self.player_2) == 1:
            self.player_1.won = True
            self.player_2.won = True
        elif len(self.player_1) > 1:
            self.player_1.won = True
        else:
            self.player_2.won = True

if __name__ == "__main__":
    game = War()
    print(game.run_game())
