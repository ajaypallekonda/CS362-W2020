import Dominion
import random
from collections import defaultdict

def theBox(nV):
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()]*10
    box["Smithy"] = [Dominion.Smithy()]*10
    box["Laboratory"] = [Dominion.Laboratory()]*10
    box["Village"] = [Dominion.Village()]*10
    box["Festival"] = [Dominion.Festival()]*10
    box["Market"] = [Dominion.Market()]*10
    box["Chancellor"] = [Dominion.Chancellor()]*10
    box["Workshop"] = [Dominion.Workshop()]*10
    box["Moneylender"] = [Dominion.Moneylender()]*10
    box["Chapel"] = [Dominion.Chapel()]*10
    box["Cellar"] = [Dominion.Cellar()]*10
    box["Remodel"] = [Dominion.Remodel()]*10
    box["Adventurer"] = [Dominion.Adventurer()]*10
    box["Feast"] = [Dominion.Feast()]*10
    box["Mine"] = [Dominion.Mine()]*10
    box["Library"] = [Dominion.Library()]*10
    box["Gardens"] = [Dominion.Gardens()]*nV
    box["Moat"] = [Dominion.Moat()]*10
    box["Council Room"] = [Dominion.Council_Room()]*10
    box["Witch"] = [Dominion.Witch()]*10
    box["Bureaucrat"] = [Dominion.Bureaucrat()]*10
    box["Militia"] = [Dominion.Militia()]*10
    box["Spy"] = [Dominion.Spy()]*10

    #TEST SCENARIO 1: change Dominion.Theif to Dominion.Spy 
    box["Thief"] = [Dominion.Thief()]*10
    box["Throne Room"] = [Dominion.Throne_Room()]*10
    return box

def theOrder():
    supply = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
              3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
              4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
              5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
              6:['Gold','Adventurer'],8:['Province']}
    return supply

def supply(boxlist, random10, nV, box, player_names, nC):
    supply = defaultdict(list,[(k,box[k]) for k in random10])

    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC

    return supply

def makePlayers(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))

    return players

def theWinner(vp, dcs, vpmax):
    winners=[]
    for i in vp.index:
        if vp.loc[i]==vpmax:
            winners.append(i)
    if len(winners)>1:
        winstring= ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0],'wins!'])

    print("\nGAME OVER!!!\n"+winstring+"\n")
    print(dcs)

    return winners