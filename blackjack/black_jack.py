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
import random

class Card(object):
    def __init__(self, color, value = 0):
        self.color = color
        self.value = value

    def display_card(self):
        print (str(self.value) + self.color)

class Deck(object):
    def __init__(self, number_of_cards):
        self.number_of_cards = int(number_of_cards)
        self.card_list = []
        self.club_list = []
        self.diamond_list = []
        self.heart_list = []
        self.spade_list = []

        self.fill_deck()
        print(str(self.number_of_cards) + " cards - " + str(len((self.card_list))) + " " + self.card_list[0].color + self.card_list[0].value)

    def card_value_generator(self):
        card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10" "Jack", "Queen", "King", "Ace"]
        random_value = random.randrange(0, len(card_value))
        card_value.remove(card_value[random_value])
        return card_value[random_value]

    def fill_deck(self):
        if self.number_of_cards > 4:
            quater_deck = 0
            quater_deck = self.number_of_cards // 4
            if quater_deck * 4 != self.number_of_cards:
                #needs fixig
                first_quater_deck = quater_deck + 1
                for club_card in range(first_quater_deck):
                    club_card = Card("Club")
                    self.card_list.append(club_card)
            else:
                for club_card in range(quater_deck):
                    club_card = Card("Club", self.card_value_generator())
                    self.card_list.append(club_card)
        else:
            pass

deck = Deck(12)
# print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# top_card = deck.draw()
# print(top_card)
# print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades
