from card_class import Card 
# from player_class import Player
from random import shuffle
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Deck:
    def __init__(self):
        self.cards = []
        self.table_cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle_deck(self):
        shuffle(self.cards)
    
    def distribute_cards(self, player1, player2):
        for i in range(26):
            player1.cards.append(self.cards[i])
        for i in range(26, 52):
            player2.cards.append(self.cards[i])
        

