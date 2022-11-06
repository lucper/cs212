#!/usr/bin/env python

## a 'card' has a rank (A,K,Q,J,2,...,10) and a suit (spades, hearts, diamonds, clubs)
## a 'hand' is a list of 5 cards
## 'straight': 5 consecutive ranks
## 'flush': 5 cards of same suit
## 'n-kind': n cards with same rank

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
