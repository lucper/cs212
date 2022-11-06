#!/usr/bin/env python

## A 'card' has a rank (A,K,Q,J,2,...,10) and a suit (spades, hearts, diamonds, clubs)
##   '<rank><suit>'
## A 'hand' is a list of 5 cards
##   ['<rank><suit>', '<rank><suit>', '<rank><suit>', '<rank><suit>', '<rank><suit>']
##
## 'straight': 5 consecutive ranks
## 'flush': 5 cards of same suit
## 'n-kind': n cards with same rank
##
## rank 8 = straight flush (same suit + consecutive ranks)
##   (8, <highest rank>)
## rank 7 = 4-kind
##   (7, <rank of 4-kind>, <rank of diff card>)
## rank 6 = "full house" = 3-kind + 2-kind
##   (6, <rank 3-kind>, <rank 2-kind>)
## rank 5 = flush
##  (5, <[all 5 cards to break tie]>)
## rank 4 = straight
##  (4, <highest rank>)
## rank 3 = 3-kind + 2 random
##  (3, <rank of 3-kind>, [2 cards])
## rank 2 = 2-kind + 2-kind + 1 random
##  (2, <rank of 2-kind>, <rank of 2-kind>, [put the two 2-kinds and 13?])
## rank 1 = 2-kind + 3 random
##  (1, <rank of 2-kind>, [rank of 2-kind up to 13?])
## rank 0 = all random
##  (0, [all ranks])

def hand_rank(hand):
    return None

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

## tests ##
def test():
    "Test cases"
    straight_flush = ['6C', '7C', '8C', '9C', 'TC']
    four_kind = ['9D', '9H', '9S', '9C', '7D']
    full_house = ['TD', 'TC', 'TH', '7C', '7D']
    assert poker([four_kind]) == four_kind
    assert poker([full_house, full_house]) == full_house
    assert poker([four_kind, full_house]) == full_house
    assert poker([straight_flush, four_kind, full_house]) == straight_flush
    assert poker([sf] + 99 * [fh]) == sf
    return "tests pass"
print(test())
##########
