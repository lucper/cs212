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

def straight(ranks):
    "Check whether the ranks are consecutive"
    return all(a < b for a, b in zip(sorted(ranks), sorted(ranks)[1:]))

def flush(hand):
    "Check whether all suits are the same"
    #if len(hand) == 1:
    #    return hand[0][1]
    #else:
    #    return hand[0][1] == flush(hand[1:])
    return len(set([s for r, s in hand])) == 1

def kind(n, ranks):
    "Check whether there are n repeated items in ranks; return the rank if true, otherwise False"
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    res = {r for r in ranks if ranks.count(r) == 2}
    if len(res) == 2:
        return max(res), min(res)
    return None

def card_ranks(hand):
    "Return ranks of a hand: card_ranks([...]) => 1..13 (2,..,10,A,K,Q,J)"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks

def hand_rank(hand):
    "Return integer indicating rank of a hand: hand_rank([...]) => 0..8"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks))
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

## tests ##
def test():
    "Test cases"
    straight_flush = ['6C', '7C', '8C', '9C', 'TC']
    four_kind = ['9D', '9H', '9S', '9C', '7D']
    full_house = ['TD', 'TC', 'TH', '7C', '7D']
    two_pairs = ['5S', '5D', '9H', '9C', '6S']
    fkranks = card_ranks(four_kind)
    tpranks = card_ranks(two_pairs)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(straight_flush) == True
    assert flush(four_kind) == False
    assert card_ranks(straight_flush) == [10, 9, 8, 7, 6]
    assert card_ranks(four_kind) == [9, 9, 9, 9, 7]
    assert card_ranks(full_house) == [10, 10, 10, 7, 7]
    assert poker([four_kind]) == four_kind
    assert poker([full_house, full_house]) == full_house
    assert poker([four_kind, full_house]) == four_kind
    assert poker([straight_flush, four_kind, full_house]) == straight_flush
    assert poker([straight_flush] + 99 * [full_house]) == straight_flush
    assert hand_rank(straight_flush) == (8, 10)
    assert hand_rank(four_kind) == (7, 9, 7)
    assert hand_rank(full_house) == (6, 10, 7)
    return "tests pass"
print(test())
##########
