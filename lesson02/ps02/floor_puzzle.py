#!/usr/bin/env python

# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  

import itertools

floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]

def higher(x, y):
    return x - y > 0

def adjacent(x, y):
    return abs(x - y) == 1

def floor_puzzle():
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
            for Hopper, Kay, Liskov, Perlis, Ritchie in itertools.permutations(floors)
            if Hopper != top
            if Kay != bottom
            if Liskov != top
            if Liskov != bottom
            if higher(Perlis, Kay)
            if not adjacent(Ritchie, Liskov)
            if not adjacent(Liskov, Kay))

print(floor_puzzle())
