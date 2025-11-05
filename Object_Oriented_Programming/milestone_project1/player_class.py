from deck_class import Deck
from card_class import values
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def take_turn(self, new_deck):
        current_card = self.cards.pop()
        print(f"{self.name} throws {current_card}")
        new_deck.table_cards.append(current_card)
        if len(new_deck.table_cards)>1 and new_deck.table_cards[-1].value > new_deck.table_cards[-2].value:
            self.cards.extend(new_deck.table_cards)
            new_deck.table_cards = []
        print(f"{self.name} is having {len(self.cards)} cards")

