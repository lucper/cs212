#!/usr/bin/env python

from itertools import combinations
from poker import *

black_suits = [r+s for r in '23456789TJQKA' for s in 'CS']
red_suits = [r+s for r in '23456789TJQKA' for s in 'HD']

def best_wild_hand_aux(hand):
    best_hand, best_rank = None, (0,)
    for bcard in black_suits:
        for rcard in red_suits:
            newhand = tuple(' '.join(hand).replace('?B', bcard).replace('?R', rcard).split())
            curr_rank = hand_rank(newhand)
            if curr_rank > best_rank:
                best_hand, best_rank = newhand, curr_rank
    return best_hand, best_rank

def best_wild_hand(cards):
    best_hand, best_rank = None, (0,)
    for hand in combinations(cards, 5):
        if '?B' in hand or '?R' in hand:
            hand, curr_rank = best_wild_hand_aux(hand)
        else:
            curr_rank = hand_rank(hand)

        if curr_rank > best_rank:
            best_hand, best_rank = hand, curr_rank
    return best_hand

r1 = best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())
r2 = best_wild_hand("TD TC 5H 7C 7D ?R ?B".split())
r3 = best_wild_hand("TD TC TH 7C 7D 7S 7H".split())

assert sorted(r1) == ['7C', '8C', '9C', 'JC', 'TC'], sorted(r1)
assert sorted(r2) == ['7C', 'TC', 'TD', 'TH', 'TS'], sorted(r2)
assert sorted(r3) == ['7C', '7D', '7H', '7S', 'TD'], sorted(r3)
