#!/usr/bin/env python
'''
1) There are five houses.
2) The Englishman lives in the red house.
3) The Spaniard owns the dog.
4) Coffee is drunk in the green house.
5) The Ukrainian drinks tea.
6) The green house is immediately to the right of the ivory house.
7) The Old Gold smoker owns snails.
8) Kools are smoked in the yellow house.
9) Milk is drunk in the middle house.
10) The Norwegian lives in the first house.
11) The man who smokes Chesterfields lives in the house next to the man with the fox.
12) Kools are smoked in the house next to the house where the horse is kept.
13) The Lucky Strike smoker drinks orange juice.
14) The Japanese smokes Parliaments.
15) The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?
'''

import time
import itertools

# houses: [red, yellow, ivory, blue, green] ==> labelled 1, 2, 3, 4, and 5
# people: [Englishman, Spaniard, Norwegian, Japanese, Ukrainian]
# smokes: [Old Gold, Parliaments, Chesterfields, Kools, Lucky Strike]
# animal: [fox, ZEBRA, snails, horse, dog]
# drinks: [juice, coffee, milk, WATER, tea]

# Tools
def timedcall(fn, *args):
    start = time.time()
    fn(*args)
    end = time.time()
    print(f'{(end - start):.3f}')

## accessed by countedcall and zebra_puzzle
def c(sequence):
    c.starts += 1 # need to be initialized beforehand
    for item in sequence:
        c.items += 1
        yield item

def countedcall(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print(f'{fn.__name__} {result} {c.starts} {c.items}')


# Aux. functions
def nextto(i, j):
    return abs(i - j) == 1

def rightto(i, j):
    '''We assume the houses are arranged as 1, 2, 3, 4, and 5.'''
    return i - j == 1

def zebra_puzzle():
    assignments = list(itertools.permutations(range(1,6)))
    return next((water, zebra)
            for red, yellow, ivory, blue, green in assignments
            if rightto(green, ivory) # 6
            for englishman, spaniard, norwegian, japanese, ukranian in assignments
            if englishman == red # 2
            if norwegian == 1 # 10
            if nextto(norwegian, blue) # 15
            for oldgold, parliments, chesterfields, kools, luckystrike in assignments
            if kools == yellow #8
            if japanese == parliments # 14
            for fox, zebra, snails, horse, dog in assignments
            if spaniard == dog # 3
            if oldgold == snails # 7
            if nextto(chesterfields, fox) # 11
            if nextto(kools, horse) # 12
            for juice, coffee, milk, water, tea in assignments
            if coffee == green # 4
            if ukranian == tea # 5
            if milk == 3 # 9
            if luckystrike == juice # 13
            )

water, zebra = zebra_puzzle()
print(f'water in house {water} and zebra in house {zebra}')
#countedcall(zebra_puzzle)
