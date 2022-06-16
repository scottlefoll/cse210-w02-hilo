# from game.card import Card


# class Deck:
#     """A group of 52 American playing cards."

#     The responsibility of Deck is to create and maintain the deck of cards, 
#     including the value and points associated with the cards.

#     Attributes:
#         value (int): The number of spots on the side facing up.
#     """

#     def __init__(self):
#         """Constructs a new instance of Card.

#         Args:
#             self (Card): An instance of Card.
#         """
#         self.value = 0
#         self.points = 0

#     def deal_card(self):
#         """Generates a new random value and calculates the points for the card.

#         Args:
#             self (Card): An instance of Card.
#         """
#         self.value = random.randint(1, 14)
#         self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0


# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]