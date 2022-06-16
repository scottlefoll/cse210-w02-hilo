from game.card import Card
import os
# from game.player import Player
# from game.deck import Deck


class Dealer:
    """A person who deals the cards, keeps score and directs the game.

    The responsibility of a Dealer is to control the cards and the play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        prior_card (int): The value of the card that was last dealt.
        new_card (int): The value of the card that was just dealt.
        total_score (int): The score for the entire game.
        guess: the user's guess for the next card.

    Methods:
        __init__ (): Initializes the Dealer.
        start_game (): Starts the game.
        do_updates (): Updates the score.
        do_inputs (): Gets the user's input.
        do_outputs (): Displays the cards and the score.
        clear (): Clears the terminal.
    """

    def __init__(self):
        """Constructs a new Dealer.

        Args:
            self (Dealer): an instance of Dealer.
        """
        self.clear()
        self.cards = []
        self.is_playing = True
        self.guess = ""
        self.total_score = 300

        for i in range(2):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to get a card.

        Args:
            self (Dealer): An instance of Dealer.
        """

        if not self.is_playing:
            return

        print(f"The card is: {self.cards[0].value}")

        while True:
            self.guess = input(f"Higher or lower? [h/l]: ").lower()
            if self.guess not in ('h', 'l'):
                print("Please enter either 'h' or 'l'.")
            else:
                break

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return

        if self.cards[1].value > self.cards[0].value and self.guess == "h":
            self.total_score += 100
        elif self.cards[1].value < self.cards[0].value and self.guess == "l":
            self.total_score += 100
        else:
            self.total_score -= 75

    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want
        get another card.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.cards[1].value}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.total_score > 0)
        if self.total_score < 1: self.is_playing = False
        if not self.is_playing: return

        while True:
            get_card = input("Play again? [y/n] ").lower()
            if get_card not in ('y', 'n'):
                print("Please enter either 'y' or 'n'.")
                continue
            if get_card == 'n':
                self.is_playing = False
                return
            else:
                self.clear()
                break

        self.cards.pop(0)
        card = Card()
        self.cards.append(card)
        return

    def clear(self):
        """clear the terminal

            Args:
                none.
            """
        os.system("cls" if os.name == "nt" else "clear")
