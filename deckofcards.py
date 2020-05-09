import random

class Deck:
     def __init__(self):
         self.suit = ["Club", "Diamond", "Heart","Spade"]
         self.rank = ["2", "3", "4", "5", "6", "7", "8","9","10","Jack","Queen", "king", "Ace"]
         self.cards = []
     
     def packofcards(self):
         for suit in self.suit:
             for rank in self.rank:
                 self.cards.append(rank + " of " + suit)
         return self.cards
      
     def shuffle_cards(self):
         shuffle_cards = random.sample(self.packofcards(), 36)

         print("the cards distributed to 4 players are:{shuffle_cards}")
         player1 = shuffle_cards[:9]
         player2 = shuffle_cards[9:18]
         player3 = shuffle_cards[18:27]
         player4 = shuffle_cards[27:]
  
         print("player1:", player1)
         print("player2:", player2)
         print("player3:", player3)
         print("player4:", player4)
obj_of_deck = Deck()
obj_of_deck.shuffle_cards()
 
 
