# class Player:
#     """A player who is asks to start the game, continues playing the game, 
#     asks for cards, makes a guess for "higher" or "lower", and leaves the game.

#     The responsibility of a player is to play the game, and follow the Dealer.

#     Attributes:
#         is_playing (boolean): Whether or not the game is being played.
#         guess (string): The user's guess for if the next card will be higher or 
#         lower than the last card.
#         name (string): The user's name.
#     """


#     def __init__(self):
#         """Constructs a new Player.

#         Args:
#             self (Player): an instance of Player.
#         """

#         self.is_playing = True
#         self.guess = 0
#         self.name = ""


#     def get_name_input(self):
#         """Ask the user to enter their name.

#         Args:
#             self (Player): An instance of Player.
#         """

#         while True:
#             self.name = input("Please enter your first name: ").capitalize
#             if not self.name.isalpha():
#                 print("Please enter letters only.")
#                 continue
#             else:
#                 break
