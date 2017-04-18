# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades

class Card(object):
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def display_card(self):
        print (str(self.value) + self.color)

class Deck(object):
    def __init__(self, number_of_cards):
        self.number_of_cards = int(number_of_cards)
        self.card_list = []
        self.fill_deck()

    def fill_deck(self):
        if self.number_of_cards > 4:
            quater_deck = self.number_of_cards // 4
            print(quater_deck)
        else:
            pass

deck = Deck(12)
print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# top_card = deck.draw()
# print(top_card)
# print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades
