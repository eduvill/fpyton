# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:19:58 2019

@author: shkim
"""
#%%
import collections

#%%
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

#%%   
if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    beer_card
    print(beer_card)

#%%    
    deck = FrenchDeck()
    #print(deck)  #<__main__.FrenchDeck object at 0x000001A92BF0D0F0>
    
    len(deck)  # __len__ called
    
    # __getitem called
    print(deck[0])
    print(deck[-1])

#%%
    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    
#%%
    # __getitem__ called
    
    print(deck[:3])      
    print(deck[9:13])
    print(deck[9::13])
   
#%%
    # __getitem__ called
    for card in deck:
        print(card)
    
#%%
    # __getitem__ called
    for card in reversed(deck):
        print(card)
    
#%%
    print(Card('A', 'hearts') in deck)
    print(Card('A', 'heart') in deck)
    
#%%
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    
    for card in sorted(deck, key=spades_high):
        print(card)
    
    
#%%