#!/usr/bin/env python

import random

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
    return all(a < b and b - a == 1 for a, b in zip(sorted(ranks), sorted(ranks)[1:]))

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
    ranks = ['-A23456789TJQK-'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks
    #return ranks[1:] + [1] if ranks[0] == 14 else ranks

def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def hand_rank(hand):
    groups = group(['-A23456789TJQK-'.index(r) for r, _ in hand])
    counts, ranks = zip(*groups)
    return (9 if (5,) == counts else
            8 if straight(ranks) and flush(hand) else
            7 if (4,1) == counts else
            6 if (3,2) == counts else
            5 if flush(hand) else
            4 if straight(ranks) else
            3 if (3,1,1) == counts else
            2 if (2,2,1) == counts else
            1 if (2,1,1,1) == counts else
            0), ranks

def allmax(iterable, key=(lambda k: k)):
    return [i for i in iterable if key(i) == key(max(iterable, key=key))]

def poker(hands):
    "Return the best hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
