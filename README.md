# War (card game)
Requirements:
```
python version 3
```

To play the game:
```
git clone https://github.com/shubhakarreddy/intel.git
cd intel
python -m game

python -m game -h (--help) for more help.
```

To run tests:
```
python -m unittest
```

### Game description
[War](https://en.wikipedia.org/wiki/War_(card_game))

### Assumptions
- Game terminates when one or both user(s) run out of cards or is left with only one card in a war scenario.
- The user does **not** play the last remaining card face-up.
- User with more cards at the end wins the game.
- Game reaches a tie when the players go to war and both are left with one card each.
- Player_1 always goes first. So general order of played cards is \[card_1, card_2\].
- Cards won are added to the bottom of the deck.
- When player_2 wins (not in a war scenario) he adds the cards in \[card_2, card_1\] order to the bottom of his deck instead of the general order. This is done to avoid the swapping of whole deck between the players when they win alternative turns which leads to an infinite loop.

### Further changes
- Add more variations of the game and give the user the choice to pick a specific variant through command line options.
- Add code coverage for tests to keep track of tested code.
