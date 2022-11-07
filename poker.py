#!/usr/bin/env python

import random

def straight(ranks):
    "Check whether the ranks are consecutive"
    return all(a < b and b - a == 1 for a, b in zip(sorted(ranks), sorted(ranks)[1:]))

def flush(hand):
    "Check whether all suits are the same"
    return len(set([s for r, s in hand])) == 1

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
            0), *ranks

def allmax(iterable, key=(lambda k: k)):
    return [i for i in iterable if key(i) == key(max(iterable, key=key))]

def poker(hands):
    "Return the best hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
