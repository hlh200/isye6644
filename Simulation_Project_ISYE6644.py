# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# BlackJack Strategy Simulation
# By Hong Lap Ivan Ho
# ISYE 6644 Simulation Project Fall 2020


# function to generate a random card from a deck
# Most casinos use 6 decks in blackjack
# Some casinos starting to use 8 decks

# Generate a random card
# Using python package to randomly generate a number from 0-511)
# 511 cards because we use six decks
# 52 cards per deck x 6 = 512

# Create the deck dictionary

#from random import randint
import random

suits = {
    0: 'Diamonds',
    1: 'Clubs',
    2: 'Hearts',
    3: 'Spades'
}

cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}

# Most Casino plays 6 decks

decks = {
    0: 'Deck 1',
    1: 'Deck 2',
    2: 'Deck 3',
    3: 'Deck 4',
    4: 'Deck 5',
    5: 'Deck 6'
}
'''
decks = {
    0: 'Deck 1'
}
'''
# strategy_chart_dictionary
# there are two elements for the key
# first is the user combined count or cards
# second is dealer's up card
# based on available information on the table, make a decision with better odds to win
strategy_dict = {
    ###
    ('5', '2') : 'Hit',
    ('5', '3') : 'Hit',
    ('5', '4') : 'Hit',
    ('5', '5') : 'Hit',
    ('5', '6') : 'Hit',
    ('5', '7') : 'Hit',
    ('5', '8') : 'Hit',
    ('5', '9') : 'Hit',
    ('5', '10') : 'Hit',
    ('5', 'Jack') : 'Hit',
    ('5', 'Queen') : 'Hit',
    ('5', 'King') : 'Hit',
    ('5', 'Ace') : 'Hit',
    ###
    ('6', '2') : 'Hit',
    ('6', '3') : 'Hit',
    ('6', '4') : 'Hit',
    ('6', '5') : 'Hit',
    ('6', '6') : 'Hit',
    ('6', '7') : 'Hit',
    ('6', '8') : 'Hit',
    ('6', '9') : 'Hit',
    ('6', '10') : 'Hit',
    ('6', 'Jack') : 'Hit',
    ('6', 'Queen') : 'Hit',
    ('6', 'King') : 'Hit',
    ('6', 'Ace') : 'Hit',
        ###
    ('7', '2') : 'Hit',
    ('7', '3') : 'Hit',
    ('7', '4') : 'Hit',
    ('7', '5') : 'Hit',
    ('7', '6') : 'Hit',
    ('7', '7') : 'Hit',
    ('7', '8') : 'Hit',
    ('7', '9') : 'Hit',
    ('7', '10') : 'Hit',
    ('7', 'Jack') : 'Hit',
    ('7', 'Queen') : 'Hit',
    ('7', 'King') : 'Hit',
    ('7', 'Ace') : 'Hit',
            ###
    ('8', '2') : 'Hit',
    ('8', '3') : 'Hit',
    ('8', '4') : 'Hit',
    ('8', '5') : 'Hit',
    ('8', '6') : 'Hit',
    ('8', '7') : 'Hit',
    ('8', '8') : 'Hit',
    ('8', '9') : 'Hit',
    ('8', '10') : 'Hit',
    ('8', 'Jack') : 'Hit',
    ('8', 'Queen') : 'Hit',
    ('8', 'King') : 'Hit',
    ('8', 'Ace') : 'Hit',
    ###
    ('9', '2') : 'Hit',
    ('9', '3') : 'Double',
    ('9', '4') : 'Double',
    ('9', '5') : 'Double',
    ('9', '6') : 'Double',
    ('9', '7') : 'Hit',
    ('9', '8') : 'Hit',
    ('9', '9') : 'Hit',
    ('9', '10') : 'Hit',
    ('9', 'Jack') : 'Hit',
    ('9', 'Queen') : 'Hit',
    ('9', 'King') : 'Hit',
    ('9', 'Ace') : 'Hit',
    ###
    ('10', '2') : 'Double',
    ('10', '3') : 'Double',
    ('10', '4') : 'Double',
    ('10', '5') : 'Double',
    ('10', '6') : 'Double',
    ('10', '7') : 'Double',
    ('10', '8') : 'Double',
    ('10', '9') : 'Double',
    ('10', '10') : 'Hit',
    ('10', 'Jack') : 'Hit',
    ('10', 'Queen') : 'Hit',
    ('10', 'King') : 'Hit',
    ('10', 'Ace') : 'Hit',    
        ###
    ('11', '2') : 'Double',
    ('11', '3') : 'Double',
    ('11', '4') : 'Double',
    ('11', '5') : 'Double',
    ('11', '6') : 'Double',
    ('11', '7') : 'Double',
    ('11', '8') : 'Double',
    ('11', '9') : 'Double',
    ('11', '10') : 'Double',
    ('11', 'Jack') : 'Double',
    ('11', 'Queen') : 'Double',
    ('11', 'King') : 'Double',
    ('11', 'Ace') : 'Hit',   
            ###
    ('12', '2') : 'Hit',
    ('12', '3') : 'Hit',
    ('12', '4') : 'Stand',
    ('12', '5') : 'Stand',
    ('12', '6') : 'Stand',
    ('12', '7') : 'Hit',
    ('12', '8') : 'Hit',
    ('12', '9') : 'Hit',
    ('12', '10') : 'Hit',
    ('12', 'Jack') : 'Hit',
    ('12', 'Queen') : 'Hit',
    ('12', 'King') : 'Hit',
    ('12', 'Ace') : 'Hit',  
                ###
    ('13', '2') : 'Stand',
    ('13', '3') : 'Stand',
    ('13', '4') : 'Stand',
    ('13', '5') : 'Stand',
    ('13', '6') : 'Stand',
    ('13', '7') : 'Hit',
    ('13', '8') : 'Hit',
    ('13', '9') : 'Hit',
    ('13', '10') : 'Hit',
    ('13', 'Jack') : 'Hit',
    ('13', 'Queen') : 'Hit',
    ('13', 'King') : 'Hit',
    ('13', 'Ace') : 'Hit',  
                    ###
    ('14', '2') : 'Stand',
    ('14', '3') : 'Stand',
    ('14', '4') : 'Stand',
    ('14', '5') : 'Stand',
    ('14', '6') : 'Stand',
    ('14', '7') : 'Hit',
    ('14', '8') : 'Hit',
    ('14', '9') : 'Hit',
    ('14', '10') : 'Hit',
    ('14', 'Jack') : 'Hit',
    ('14', 'Queen') : 'Hit',
    ('14', 'King') : 'Hit',
    ('14', 'Ace') : 'Hit',  
                    ###
    ('15', '2') : 'Stand',
    ('15', '3') : 'Stand',
    ('15', '4') : 'Stand',
    ('15', '5') : 'Stand',
    ('15', '6') : 'Stand',
    ('15', '7') : 'Hit',
    ('15', '8') : 'Hit',
    ('15', '9') : 'Hit',
    ('15', '10') : 'Hit',
    ('15', 'Jack') : 'Hit',
    ('15', 'Queen') : 'Hit',
    ('15', 'King') : 'Hit',
    ('15', 'Ace') : 'Hit',  
                    ###
    ('16', '2') : 'Stand',
    ('16', '3') : 'Stand',
    ('16', '4') : 'Stand',
    ('16', '5') : 'Stand',
    ('16', '6') : 'Stand',
    ('16', '7') : 'Hit',
    ('16', '8') : 'Hit',
    ('16', '9') : 'Hit',
    ('16', '10') : 'Hit',
    ('16', 'Jack') : 'Hit',
    ('16', 'Queen') : 'Hit',
    ('16', 'King') : 'Hit',
    ('16', 'Ace') : 'Hit',  
    ###
    ('17', '2') : 'Stand',
    ('17', '3') : 'Stand',
    ('17', '4') : 'Stand',
    ('17', '5') : 'Stand',
    ('17', '6') : 'Stand',
    ('17', '7') : 'Stand',
    ('17', '8') : 'Stand',
    ('17', '9') : 'Stand',
    ('17', '10') : 'Stand',
    ('17', 'Jack') : 'Stand',
    ('17', 'Queen') : 'Stand',
    ('17', 'King') : 'Stand',
    ('17', 'Ace') : 'Stand',  
    ###
    ('18', '2') : 'Stand',
    ('18', '3') : 'Stand',
    ('18', '4') : 'Stand',
    ('18', '5') : 'Stand',
    ('18', '6') : 'Stand',
    ('18', '7') : 'Stand',
    ('18', '8') : 'Stand',
    ('18', '9') : 'Stand',
    ('18', '10') : 'Stand',
    ('18', 'Jack') : 'Stand',
    ('18', 'Queen') : 'Stand',
    ('18', 'King') : 'Stand',
    ('18', 'Ace') : 'Stand',      
        ###
    ('19', '2') : 'Stand',
    ('19', '3') : 'Stand',
    ('19', '4') : 'Stand',
    ('19', '5') : 'Stand',
    ('19', '6') : 'Stand',
    ('19', '7') : 'Stand',
    ('19', '8') : 'Stand',
    ('19', '9') : 'Stand',
    ('19', '10') : 'Stand',
    ('19', 'Jack') : 'Stand',
    ('19', 'Queen') : 'Stand',
    ('19', 'King') : 'Stand',
    ('19', 'Ace') : 'Stand', 
        ###
    ('20', '2') : 'Stand',
    ('20', '3') : 'Stand',
    ('20', '4') : 'Stand',
    ('20', '5') : 'Stand',
    ('20', '6') : 'Stand',
    ('20', '7') : 'Stand',
    ('20', '8') : 'Stand',
    ('20', '9') : 'Stand',
    ('20', '10') : 'Stand',
    ('20', 'Jack') : 'Stand',
    ('20', 'Queen') : 'Stand',
    ('20', 'King') : 'Stand',
    ('20', 'Ace') : 'Stand', 
    ########################
    ('A,2', '2') : 'Hit',
    ('A,2', '3') : 'Hit',
    ('A,2', '4') : 'Hit',
    ('A,2', '5') : 'Double',
    ('A,2', '6') : 'Double',
    ('A,2', '7') : 'Hit',
    ('A,2', '8') : 'Hit',
    ('A,2', '9') : 'Hit',
    ('A,2', '10') : 'Hit',
    ('A,2', 'Jack') : 'Hit',
    ('A,2', 'Queen') : 'Hit',
    ('A,2', 'King') : 'Hit',
    ('A,2', 'Ace') : 'Hit',
    ###
    ('A,3', '2') : 'Hit',
    ('A,3', '3') : 'Hit',
    ('A,3', '4') : 'Hit',
    ('A,3', '5') : 'Double',
    ('A,3', '6') : 'Double',
    ('A,3', '7') : 'Hit',
    ('A,3', '8') : 'Hit',
    ('A,3', '9') : 'Hit',
    ('A,3', '10') : 'Hit',
    ('A,3', 'Jack') : 'Hit',
    ('A,3', 'Queen') : 'Hit',
    ('A,3', 'King') : 'Hit',
    ('A,3', 'Ace') : 'Hit',
        ###
    ('A,4', '2') : 'Hit',
    ('A,4', '3') : 'Hit',
    ('A,4', '4') : 'Double',
    ('A,4', '5') : 'Double',
    ('A,4', '6') : 'Double',
    ('A,4', '7') : 'Hit',
    ('A,4', '8') : 'Hit',
    ('A,4', '9') : 'Hit',
    ('A,4', '10') : 'Hit',
    ('A,4', 'Jack') : 'Hit',
    ('A,4', 'Queen') : 'Hit',
    ('A,4', 'King') : 'Hit',
    ('A,4', 'Ace') : 'Hit',
    ###
    ('A,5', '2') : 'Hit',
    ('A,5', '3') : 'Hit',
    ('A,5', '4') : 'Double',
    ('A,5', '5') : 'Double',
    ('A,5', '6') : 'Double',
    ('A,5', '7') : 'Hit',
    ('A,5', '8') : 'Hit',
    ('A,5', '9') : 'Hit',
    ('A,5', '10') : 'Hit',
    ('A,5', 'Jack') : 'Hit',
    ('A,5', 'Queen') : 'Hit',
    ('A,5', 'King') : 'Hit',
    ('A,5', 'Ace') : 'Hit',
        ###
    ('A,6', '2') : 'Hit',
    ('A,6', '3') : 'Double',
    ('A,6', '4') : 'Double',
    ('A,6', '5') : 'Double',
    ('A,6', '6') : 'Double',
    ('A,6', '7') : 'Hit',
    ('A,6', '8') : 'Hit',
    ('A,6', '9') : 'Hit',
    ('A,6', '10') : 'Hit',
    ('A,6', 'Jack') : 'Hit',
    ('A,6', 'Queen') : 'Hit',
    ('A,6', 'King') : 'Hit',
    ('A,6', 'Ace') : 'Hit',
          ###
    ('A,7', '2') : 'Stand',
    ('A,7', '3') : 'Double',
    ('A,7', '4') : 'Double',
    ('A,7', '5') : 'Double',
    ('A,7', '6') : 'Double',
    ('A,7', '7') : 'Stand',
    ('A,7', '8') : 'Stand',
    ('A,7', '9') : 'Hit',
    ('A,7', '10') : 'Hit',
    ('A,7', 'Jack') : 'Hit',
    ('A,7', 'Queen') : 'Hit',
    ('A,7', 'King') : 'Hit',
    ('A,7', 'Ace') : 'Stand',  
            ###
    ('A,8', '2') : 'Stand',
    ('A,8', '3') : 'Stand',
    ('A,8', '4') : 'Stand',
    ('A,8', '5') : 'Stand',
    ('A,8', '6') : 'Stand',
    ('A,8', '7') : 'Stand',
    ('A,8', '8') : 'Stand',
    ('A,8', '9') : 'Stand',
    ('A,8', '10') : 'Stand',
    ('A,8', 'Jack') : 'Stand',
    ('A,8', 'Queen') : 'Stand',
    ('A,8', 'King') : 'Stand',
    ('A,8', 'Ace') : 'Stand',  
                ###
    ('A,9', '2') : 'Stand',
    ('A,9', '3') : 'Stand',
    ('A,9', '4') : 'Stand',
    ('A,9', '5') : 'Stand',
    ('A,9', '6') : 'Stand',
    ('A,9', '7') : 'Stand',
    ('A,9', '8') : 'Stand',
    ('A,9', '9') : 'Stand',
    ('A,9', '10') : 'Stand',
    ('A,9', 'Jack') : 'Stand',
    ('A,9', 'Queen') : 'Stand',
    ('A,9', 'King') : 'Stand',
    ('A,9', 'Ace') : 'Stand',  
    ###
    ('A,10', '2') : 'Stand',
    ('A,10', '3') : 'Stand',
    ('A,10', '4') : 'Stand',
    ('A,10', '5') : 'Stand',
    ('A,10', '6') : 'Stand',
    ('A,10', '7') : 'Stand',
    ('A,10', '8') : 'Stand',
    ('A,10', '9') : 'Stand',
    ('A,10', '10') : 'Stand',
    ('A,10', 'Jack') : 'Stand',
    ('A,10', 'Queen') : 'Stand',
    ('A,10', 'King') : 'Stand',
    ('A,10', 'Ace') : 'Stand',  
    ###########################
    ('2,2', '2') : 'Split',
    ('2,2', '3') : 'Split',
    ('2,2', '4') : 'Split',
    ('2,2', '5') : 'Split',
    ('2,2', '6') : 'Split',
    ('2,2', '7') : 'Split',
    ('2,2', '8') : 'Hit',
    ('2,2', '9') : 'Hit',
    ('2,2', '10') : 'Hit',
    ('2,2', 'Jack') : 'Hit',
    ('2,2', 'Queen') : 'Hit',
    ('2,2', 'King') : 'Hit',
    ('2,2', 'Ace') : 'Hit',
    #####
    ('3,3', '2') : 'Split',
    ('3,3', '3') : 'Split',
    ('3,3', '4') : 'Split',
    ('3,3', '5') : 'Split',
    ('3,3', '6') : 'Split',
    ('3,3', '7') : 'Split',
    ('3,3', '8') : 'Hit',
    ('3,3', '9') : 'Hit',
    ('3,3', '10') : 'Hit',
    ('3,3', 'Jack') : 'Hit',
    ('3,3', 'Queen') : 'Hit',
    ('3,3', 'King') : 'Hit',
    ('3,3', 'Ace') : 'Hit',
        #####
    ('4,4', '2') : 'Hit',
    ('4,4', '3') : 'Hit',
    ('4,4', '4') : 'Hit',
    ('4,4', '5') : 'Split',
    ('4,4', '6') : 'Split',
    ('4,4', '7') : 'Hit',
    ('4,4', '8') : 'Hit',
    ('4,4', '9') : 'Hit',
    ('4,4', '10') : 'Hit',
    ('4,4', 'Jack') : 'Hit',
    ('4,4', 'Queen') : 'Hit',
    ('4,4', 'King') : 'Hit',
    ('4,4', 'Ace') : 'Hit',
            #####
    ('5,5', '2') : 'Double',
    ('5,5', '3') : 'Double',
    ('5,5', '4') : 'Double',
    ('5,5', '5') : 'Double',
    ('5,5', '6') : 'Double',
    ('5,5', '7') : 'Double',
    ('5,5', '8') : 'Double',
    ('5,5', '9') : 'Double',
    ('5,5', '10') : 'Double',
    ('5,5', 'Jack') : 'Double',
    ('5,5', 'Queen') : 'Double',
    ('5,5', 'King') : 'Double',
    ('5,5', 'Ace') : 'Double',
                #####
    ('6,6', '2') : 'Split',
    ('6,6', '3') : 'Split',
    ('6,6', '4') : 'Split',
    ('6,6', '5') : 'Split',
    ('6,6', '6') : 'Split',
    ('6,6', '7') : 'Hit',
    ('6,6', '8') : 'Hit',
    ('6,6', '9') : 'Hit',
    ('6,6', '10') : 'Hit',
    ('6,6', 'Jack') : 'Hit',
    ('6,6', 'Queen') : 'Hit',
    ('6,6', 'King') : 'Hit',
    ('6,6', 'Ace') : 'Hit',
    ####
    ('7,7', '2') : 'Split',
    ('7,7', '3') : 'Split',
    ('7,7', '4') : 'Split',
    ('7,7', '5') : 'Split',
    ('7,7', '6') : 'Split',
    ('7,7', '7') : 'Split',
    ('7,7', '8') : 'Hit',
    ('7,7', '9') : 'Hit',
    ('7,7', '10') : 'Hit',
    ('7,7', 'Jack') : 'Hit',
    ('7,7', 'Queen') : 'Hit',
    ('7,7', 'King') : 'Hit',
    ('7,7', 'Ace') : 'Hit',
        ####
    ('8,8', '2') : 'Split',
    ('8,8', '3') : 'Split',
    ('8,8', '4') : 'Split',
    ('8,8', '5') : 'Split',
    ('8,8', '6') : 'Split',
    ('8,8', '7') : 'Split',
    ('8,8', '8') : 'Split',
    ('8,8', '9') : 'Split',
    ('8,8', '10') : 'Split',
    ('8,8', 'Jack') : 'Split',
    ('8,8', 'Queen') : 'Split',
    ('8,8', 'King') : 'Split',
    ('8,8', 'Ace') : 'Split',
            ####
    ('9,9', '2') : 'Split',
    ('9,9', '3') : 'Split',
    ('9,9', '4') : 'Split',
    ('9,9', '5') : 'Split',
    ('9,9', '6') : 'Split',
    ('9,9', '7') : 'Stand',
    ('9,9', '8') : 'Split',
    ('9,9', '9') : 'Split',
    ('9,9', '10') : 'Stand',
    ('9,9', 'Jack') : 'Stand',
    ('9,9', 'Queen') : 'Stand',
    ('9,9', 'King') : 'Stand',
    ('9,9', 'Ace') : 'Stand',
        ###
    ('10,10', '2') : 'Stand',
    ('10,10', '3') : 'Stand',
    ('10,10', '4') : 'Stand',
    ('10,10', '5') : 'Stand',
    ('10,10', '6') : 'Stand',
    ('10,10', '7') : 'Stand',
    ('10,10', '8') : 'Stand',
    ('10,10', '9') : 'Stand',
    ('10,10', '10') : 'Stand',
    ('10,10', 'Jack') : 'Stand',
    ('10,10', 'Queen') : 'Stand',
    ('10,10', 'King') : 'Stand',
    ('10,10', 'Ace') : 'Stand',  
    ####
    ('Ace,Ace', '2') : 'Split',
    ('Ace,Ace', '3') : 'Split',
    ('Ace,Ace', '4') : 'Split',
    ('Ace,Ace', '5') : 'Split',
    ('Ace,Ace', '6') : 'Split',
    ('Ace,Ace', '7') : 'Split',
    ('Ace,Ace', '8') : 'Split',
    ('Ace,Ace', '9') : 'Split',
    ('Ace,Ace', '10') : 'Split',
    ('Ace,Ace', 'Jack') : 'Split',
    ('Ace,Ace', 'Queen') : 'Split',
    ('Ace,Ace', 'King') : 'Split',
    ('Ace,Ace', 'Ace') : 'Split'    
}

# Strategy Setting and Other Config values
player_wallet = 100000.0
number_of_simulation = 100000
number_of_hands = 0
hit_till = 17
blackjack_playout_with_bet = 2.5 #2.2 for some casino
#stand_when_see_dealer = {2,3,4,5,6}
buy_insurance_when_I_have = 33 # bigger than 22 means don't buy insurance
games_dealer_won = 0
games_player_won = 0
draw_game = 0 
games_player_won_on_blackjack = 0
games_dealer_won_on_blackjack = 0
games_player_won_insurance = 0
games_player_lost_insurance = 0
split_game_count = 0
double_game_count = 0
games_player_won_on_double = 0
games_player_lost_on_double = 0

# Global variable for the hands
list_dealt = []
dealer_list = []
player_list = []
dealer_final = 0
player_final = 0
player_blackjack = False
dealer_blackjack = False
player_hand_1_blackjack = False
player_hand_2_blackjack = False
insurance_won = False
game_over = False
#cnt = 0
strategy_split = False
strategy_double = False
#players_no_of_hand = 0 
strategy = 'default'
split_hand_1_strategy = 'default'
split_hand_2_strategy =  'default'
split_hand_1_strategy_double = False
split_hand_2_strategy_double = False

# clear list of played card to refresh
def reshuffle_cards():
    list_dealt.clear()
    dealer_list.clear()
    player_list.clear()
    
def get_strategy(player_card_1, player_card_2, dealer_up_card):
    if player_card_1 in ('Jack','Queen','King'):
        player_card_1 = '10'
    if player_card_2 in ('Jack','Queen','King'):
        player_card_2 = '10'           
    # For player cards are the same
    if player_card_1 == player_card_2:
        player_str = player_card_1 + ',' + player_card_2
        
    # For player with one ace        
    elif player_card_1 == 'Ace':
        player_str = 'A' + ',' + player_card_2
    elif player_card_2 == 'Ace':
        player_str = 'A' + ',' + player_card_1
             
    # For other cases             
    else:
        player_str = str(int(player_card_1) + int(player_card_2))
                             
    return(strategy_dict.get((player_str,dealer_up_card)))

def get_strategy_str(player_str,dealer_up_card):
    return(strategy_dict.get((player_str,dealer_up_card)))    
                
def draw_cards(num_of_cards, list_dealt, individual, hand):
    for z in range(num_of_cards):        
        x = random.randint(0,3) #random integer 0 to 3 to pick suit
        y = random.randint(0,12) #random integer 0 to 12 to pick card
        d = random.randint(0,5) #random integer 0 to 5 to pick deck
        # mycard = "{0} of {1} in {2}".format(cards[y],suits[x], decks[d])
        mycard = [cards[y],suits[x], decks[d], hand]        
        #x = random.randint(0,155) #155 #51
        #mycard = [player_cards[x][0],player_cards[x][1],player_cards[x][2],hand]
        if mycard not in list_dealt:
            list_dealt.append(mycard)
            if  individual == 'dealer':
                dealer_list.append(mycard)
            else:
                player_list.append(mycard)
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards,list_dealt, individual, hand)
            # there is an error here, resolved?
            
    return list_dealt
    
# count dealer point to determine action  
def count_dealer_cards():
    dealer_cnt = 0  
    ace_cnt_as_11 = 0
    for each in dealer_list:
        if each[0] in ('King','Jack','Queen','10'):
            dealer_cnt += 10 
        elif each[0] not in ('Ace'):
            dealer_cnt = dealer_cnt + int(each[0])
        elif each[0] == 'Ace':  
            dealer_cnt += 11
            if dealer_cnt > 21:
                dealer_cnt -= 10
            else:
                ace_cnt_as_11 += 1
    while dealer_cnt > 21 and ace_cnt_as_11 >= 1:
        dealer_cnt -= 10
        ace_cnt_as_11 -= 1
    return(dealer_cnt)      


# count player point to determine action
def count_player_cards():
    player_cnt = 0
    ace_cnt_as_11 = 0
    for each in player_list:        
        if each[0] in ('King','Jack','Queen','10'):
            player_cnt += 10 
        elif each[0] not in ('Ace'):
            player_cnt = player_cnt + int(each[0])
        elif each[0] == 'Ace':  
            player_cnt += 11
            if player_cnt > 21:
                player_cnt -= 10
            else:
                ace_cnt_as_11 += 1
    while player_cnt > 21 and ace_cnt_as_11 >= 1:
        player_cnt -= 10
        ace_cnt_as_11 -= 1    
    return(player_cnt)

# count player point to determine action
def count_player_cards_by_hand(hand):
    player_cnt = 0
    ace_cnt_as_11 = 0
    for each in player_list:
        if each[3] == hand:
            if each[0] in ('King','Jack','Queen','10'):
                player_cnt += 10 
            elif each[0] not in ('Ace'):
                player_cnt = player_cnt + int(each[0])
            elif each[0] == 'Ace':  
                player_cnt += 11
                if player_cnt > 21:
                    player_cnt -= 10
                else:
                    ace_cnt_as_11 += 1
    while player_cnt > 21 and ace_cnt_as_11 >= 1:
        player_cnt -= 10
        ace_cnt_as_11 -= 1    
    return(player_cnt)

# Simulate playing X number of games
while number_of_simulation > number_of_hands:
    # hand count
    hand = 0
    
    # wallet deduct
    player_wallet -= 1
    
    
    # reset for new hand   
    reshuffle_cards()     
    player_blackjack = False      
    game_over = False
    strategy_split = False
    strategy_double = False
    dealer_blackjack = False
    insurance_won = False
    hit_till = 17
    strategy = 'default'
    split_hand_1_strategy = 'default'
    split_hand_2_strategy =  'default'
    split_hand_1_strategy_double = False
    split_hand_2_strategy_double = False
    player_hand_1_blackjack = False
    player_hand_2_blackjack = False
    
    ### Intital draw
    draw_cards(1, list_dealt, 'player',0)
    draw_cards(1, list_dealt, 'dealer',0)
    draw_cards(1, list_dealt, 'player',0)
    draw_cards(1, list_dealt, 'dealer',0)
###    print('dealer initial hand ' +  str(dealer_list))
###    print('player initial hand ' + str(player_list))
    
    ##### Table to determine decision including double ######
    ##### Change Hit till ###################################
    strategy = get_strategy(player_list[0][0], player_list[1][0], dealer_list[0][0])
###    print('strategy ' + strategy)

    strategy = 'UGA strategy' #UGA strategy
    
    if strategy == 'Stand':
        hit_till = 12
    elif strategy == 'Split':
        strategy_split = True
        player_wallet -= 1
    elif strategy == 'Double':
        strategy_double = True  
        player_wallet -= 1
    elif strategy == 'Hit':
        hit_till = hit_till     
                    
    # Dealer check blackjack before player's action
    # show one card, if it is Ace, allow player the choice to buy insurance 
    # reveal first card
    # check if want to buy insurance
    if dealer_list[0][0] == 'Ace':
        if buy_insurance_when_I_have < 22: 
            player_wallet -= 0.5
            if dealer_list[1][0] in ('King','Jack','Queen','10'):
                games_player_won_insurance += 1   
                player_wallet += 1                 
            else:
                games_player_lost_insurance += 1
        else:
            if dealer_list[1][0] in ('King','Jack','Queen','10'):
                dealer_blackjack = True 
                if count_player_cards() != 21 and strategy != 'Split':                
                    # dealer blackjack
                    games_dealer_won += 1
                    games_dealer_won_on_blackjack += 1
                    game_over = True
    if dealer_list[0][0] in ('King','Jack','Queen','10') and dealer_list[1][0] == 'Ace':
        dealer_blackjack = True                    
                
    #### Handling Split ####
    if strategy_split:
        if player_list[0][0] == player_list[1][0]:
        # split = True
            player_list[1][3] = 1
            draw_cards(1, list_dealt, 'player',0)
            draw_cards(1, list_dealt, 'player',1)   
            split_hand_1_strategy = get_strategy(player_list[0][0], player_list[2][0], dealer_list[0][0])            
            split_hand_2_strategy = get_strategy(player_list[1][0], player_list[3][0], dealer_list[0][0])
            
    if game_over == False:
        ### Player's action
        # player's strategy implement here   
        if strategy_split:
            # First hand strategy
            if split_hand_1_strategy == 'Stand':
                hit_till = 12
            elif split_hand_1_strategy == 'Double':
                split_hand_1_strategy_double = True  
                player_wallet -= 1
            elif split_hand_1_strategy == 'Hit':
                hit_till = hit_till   
            # First hand            
            if count_player_cards_by_hand(0) == 21:
                player_hand_1_blackjack = True
                # print(player_list)
            while count_player_cards_by_hand(0) < hit_till:
                draw_cards(1, list_dealt, 'player',0)
                if get_strategy_str(str(count_player_cards_by_hand(0)), dealer_list[0][0]) == 'Stand':
                    break
###            print(player_list)
            player_final_1 = count_player_cards_by_hand(0)
###            print('player final 1 ' + str(player_final_1))
            
            # Second hand strategy
            if split_hand_2_strategy == 'Stand':
                hit_till = 12
            elif split_hand_2_strategy == 'Double':
                split_hand_2_strategy_double = True
                player_wallet -= 1
            elif split_hand_2_strategy == 'Hit':
                hit_till = hit_till 
            # Second hand
            if count_player_cards_by_hand(1) == 21:
                player_hand_2_blackjack = True                
                # print('player second hand ' + player_list)
            while count_player_cards_by_hand(1) < hit_till:
                draw_cards(1, list_dealt, 'player',1)
                if get_strategy_str(str(count_player_cards_by_hand(1)), dealer_list[0][0]) == 'Stand':
                    break
###            print(player_list)
            player_final_2 = count_player_cards_by_hand(1)
###            print('player final 2 ' + str(player_final_2))
            
        else:            
            if count_player_cards() == 21:
                player_blackjack = True
                #print(player_list)
            while count_player_cards() < hit_till:
                draw_cards(1, list_dealt, 'player',0)
                if get_strategy_str(str(count_player_cards()), dealer_list[0][0]) == 'Stand':
###                    print(player_list)
                    break
###                print(player_list)
            player_final = count_player_cards()
###        print('player final ' + str(player_final))
    
        ### Dealer's action
        
        #initial_dealer_count = count_dealer_cards(dealer_list)    
        while count_dealer_cards() < 17 and player_final < 22:
            draw_cards(1, list_dealt, 'dealer',0)
###            print(dealer_list)
        
        dealer_final = count_dealer_cards()
###        print('dealer final ' + str(dealer_final))
        
        # determine winner        
        if strategy_split:
            if player_hand_1_blackjack == True and dealer_blackjack == False:
                #print(dealer_list)
                #print(player_list)
                games_player_won += 1
                games_player_won_on_blackjack += 1
                if split_hand_1_strategy_double:
                    double_game_count += 1
                    games_player_won_on_double += 1
                    player_wallet += blackjack_playout_with_bet*2    
                else:
                    player_wallet += blackjack_playout_with_bet            
            elif dealer_final > 21 or (player_final_1 > dealer_final and player_final_1 < 22):
                games_player_won += 1
                #print('player won')
                if split_hand_1_strategy_double:
                    double_game_count += 1
                    games_player_won_on_double += 1                    
                    player_wallet += 4                        
                else:
                    player_wallet += 2                    
            elif player_final_1 == dealer_final:
                draw_game += 1
                if split_hand_1_strategy_double:
                    player_wallet += 2
                else:
                    player_wallet += 1                                 
                #print('draw game') 
            else:
                games_dealer_won += 1
                if split_hand_1_strategy_double:
                    double_game_count += 1
                    games_player_lost_on_double += 1  
            ####
            if player_hand_2_blackjack == True and dealer_blackjack == False:
                games_player_won += 1
                games_player_won_on_blackjack += 1
                #print(dealer_list)
                #print(player_list)
                if split_hand_2_strategy_double:
                    double_game_count += 1
                    games_player_won_on_double += 1
                    player_wallet += blackjack_playout_with_bet*2    
                else:
                    player_wallet += blackjack_playout_with_bet            
            elif dealer_final > 21 or (player_final_2 > dealer_final and player_final_2 < 22):
                games_player_won += 1
                #print('player won')
                if split_hand_2_strategy_double:
                    double_game_count += 1
                    games_player_won_on_double += 1                
                    player_wallet += 4
                else:
                    player_wallet += 2                    
            elif player_final_2 == dealer_final:
                draw_game += 1
                if split_hand_2_strategy_double:
                    player_wallet += 2
                else:
                    player_wallet += 1                 
                #print('draw game') 
            else:
                games_dealer_won += 1
                if split_hand_2_strategy_double:
                    double_game_count += 1
                    games_player_lost_on_double += 1  
            #print('dealer_list ' + str(dealer_list))
            #print('player_list ' + str(player_list))                     
            split_game_count +=1
        else:
            if player_blackjack == True and dealer_blackjack == False:
                games_player_won += 1
                games_player_won_on_blackjack += 1
                if strategy_double:
                    double_game_count += 1
                    games_player_won_on_double += 1
                    player_wallet += blackjack_playout_with_bet*2    
                else:
                    player_wallet += blackjack_playout_with_bet
            elif dealer_final > 21 or (player_final > dealer_final and player_final < 22):
                games_player_won += 1
                if strategy_double:       
                    double_game_count += 1
                    games_player_won_on_double += 1
                    player_wallet += 4
                else:
                    player_wallet += 2
                #print('dealer_list ' + str(dealer_list))
                #print('player_list ' + str(player_list))                    
                #print('player won')
            elif player_final == dealer_final:
                draw_game += 1
                if strategy_double:
                    player_wallet += 2
                else:
                    player_wallet += 1 
                #print('draw game') 
            else:            
                games_dealer_won += 1
                if strategy_double:
                    double_game_count += 1
                    games_player_lost_on_double += 1              
                #print('dealer won') 
            #print('dealer_list ' + str(dealer_list))
            #print('player_list ' + str(player_list))
#        if player_blackjack == True and dealer_blackjack == True:
#            print('both blackjack')
        
    number_of_hands += 1
    
##################################################################################
######################### Result #################################################
print('Player Wallet - ' + str(player_wallet)) 
print('Out of ' + str(number_of_simulation) + ' games we simulated')    
print('Player won ' + str(games_player_won) + ' times')
print('Dealer won ' + str(games_dealer_won) + ' times')
print('There are ' + str(draw_game) + ' draw games')
print('Player won on blackjack ' + str(games_player_won_on_blackjack) + ' times')
print('Dealer won on blackjack ' + str(games_dealer_won_on_blackjack) + ' times')
print('Player won insurance ' + str(games_player_won_insurance) + ' times')
print('Player lost insurance ' + str(games_player_lost_insurance) + ' times')
print('Number of Split games ' + str(split_game_count) + ' ')
print('Number of Double games ' + str(double_game_count) + ' ')
print('Player won on double ' + str(games_player_won_on_double) + ' times')
print('Player lost on double ' + str(games_player_lost_on_double) + ' times')
##################################################################################
##################################################################################



