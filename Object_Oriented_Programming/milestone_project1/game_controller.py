from player_class import Player
from deck_class import Deck

def start_game():
    ''''
    This function will be responsible for handling the control of the game. Tasks like creating the deck, creating the players, distributing the cards, playing turns analysing the game, deciding the winner and finaly announcing the winned will be done here
    '''
    # Creating the deck
    new_deck = Deck()
    # Shuffling the cards in deck
    new_deck.shuffle_deck()
    # Creating player1
    player1 = Player("Player1")
    # Creating player2
    player2 = Player("Player2")
    # Card distribution between both the players
    new_deck.distribute_cards(player1, player2)
    # this object will indicate is it first players turn or second players turn
    turn_of_player = player1 
    # Running the game unless one of the player's all the cards exhaust
    while len(player1.cards)!=0 and len(player2.cards) != 0:
        turn_of_player.take_turn(new_deck)
        if turn_of_player is player1:
            turn_of_player = player2
        else:
            turn_of_player = player1
    
    if len(player1.cards) == 0:
        print("Congratulations " + player1.name + " you won the game")
        print("OOPSSS! " + player2.name + " you lost but don't loose hope try next time")
    else:
        print("Congratulations " + player2.name + " you won the game")
        print("Ooh! " + player1.name + " you lost but don't loose hope try next time")
        

start_game()
        


