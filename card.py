from random import randint


class Card:
    """A playing card with a game value of between 1 and 13.

    The responsibility of Card is to create a new card and assign its own
    value.

    Attributes:
        value (int): numerical value for the card.

    Methods:
        __init__ (): Initializes the Card.
    
    """


    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = self.value = randint(1, 14)

    # def deal_card(self):
    # def deal_card(self):
    #     """Generates a new random value for the card.
        
    #     Args:
    #         self (Card): An instance of Card.
    #     """
    #     self.value = random.randint(1, 14)
