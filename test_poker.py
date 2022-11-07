#!/usr/bin/env python

import pytest
from poker import *

@pytest.fixture
def sf():
    return ['6C', '7C', '8C', '9C', 'TC']

@pytest.fixture
def fk():
    return ['9D', '9H', '9S', '9C', '7D']

@pytest.fixture
def fh():
    return ['TD', 'TC', 'TH', '7C', '7D']

@pytest.fixture
def tp():
    return ['5S', '5D', '9H', '9C', '6S']

@pytest.fixture
def fkranks(fk):
    return card_ranks(fk)

@pytest.fixture
def tpranks(tp):
    return card_ranks(tp)

def test_2straight_beats_Ahigh():
    s1 = ['AS', '2S', '3S', '4S', '5C'] # A-5 straight
    s2 = ['2C', '3C', '4C', '5S', '6S'] # 2-6 straight
    ah = ['AS', '2S', '3S', '4S', '6C'] # A high
    sh = ['2S', '3S', '4S', '6C', '7D'] # 7 high
    assert poker([s1, s2, ah, sh]) == [s2]

def test_kind(fkranks, tpranks):
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

def test_two_pair(fkranks, tpranks):
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
    
def test_straight():
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

def test_flush(sf, fk):
    assert flush(sf) == True
    assert flush(fk) == False

def test_card_ranks(sf, fk, fh):
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

def test_poker(fk, fh, sf):
    assert poker([fk]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fk, fh]) == [fk]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([sf] + 99 * [fh]) == [sf]

def test_hand_rank(sf, fk, fh):
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
