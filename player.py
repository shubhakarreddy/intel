class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.won = False

    def __len__(self):
        return len(self.cards)

    def play(self):
        # Return the card on the top of the deck
        return self.cards.pop()

    def add_cards(self, cards):
        # Add new cards below the current deck
        self.cards = cards + self.cards

    def set_status(self, status):
        self.won = status

    def is_winner(self):
        return self.won
