__author__ = 'hjones2368'
import random

class Card:
 def __init_(self, rank, suit, rank_value):
  self._rank = rank
  self._suit = suit
  self._rank_value = rank_value

def getRankName(rank_value):
    if(rank_value == 11):
        return "Jack"
    if(rank_value == 12):
        return "Queen"
    if(rank_value == 13):
        return "King"
    if(rank_value == 14):
        return "Ace"

    return str(rank_value)



 #def setRank(self, rank):
     #self.rank = rank

 #def setSuit(self, suit):
     #self.suit = suit

class Deck():

 def Shuffle(self):
  suits  = ["Clubs", "Diamonds", "Spades", "Hearts"]
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
  deckofcards = []
  for suit in suits:
    rank_value = 2
    for rank_value in range(2,15):
       newCard = Card(suit, rank_value)
       deckofcards.append(newCard)#(str(rank) + " of " + suit)

  #random.shuffle(self.deckofcards)

  return deckofcards

def printDeck(deck):
 for card in deck:
  print("(0:s)".format(card))


 def Deal(self, Players):
     Game = []
     for x in range(0,Players):
         Game.append([])

     for hand in Game:
      while len(hand) < 5:
        hand.append(self.deckofcards.pop())

     return Game
 def Save(self, filename):
     Input = open(filename, 'w')
     Input.write(Hand)
     Input.close()

Players = input ("How many Players?")

Newgame = Deck()
Newgame.Shuffle()
Hand = Newgame.Deal(Players)
Newgame.Save('test.txt')
print (Hand)
print (Newgame.deckofcards)