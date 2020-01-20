# -*- coding: utf-8 -*-
"""
Date Modified: Sun Jan 19 2020

@author: Ajay Pallekonda
"""

#TEST SCENARIO 1: change Dominion.Thief to Dominion.Spy in the testUtility.py file
#Originally: box["Thief"] = [Dominion.Thief()]*10
#Changed to: box["Thief"] = [Dominion.Spy()]*10

#Result: player is not able to buy a thief card despite having 
#        enough buying power and available card

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.theBox(nV)
supply_order = testUtility.theOrder()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = testUtility.supply(boxlist, random10, nV, box, player_names, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.makePlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners = testUtility.theWinner(vp, dcs, vpmax)