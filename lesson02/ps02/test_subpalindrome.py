#!/usr/bin/env python

from subpalindrome import longest_subpalindrome_slice

def test():
    assert longest_subpalindrome_slice('racecar') == (0, 7)
    assert longest_subpalindrome_slice('Racecar') == (0, 7)
    assert longest_subpalindrome_slice('RacecarX') == (0, 7)
    assert longest_subpalindrome_slice('Race carr') == (7, 9)
    assert longest_subpalindrome_slice('') == (0, 0)
    assert longest_subpalindrome_slice('something rac e car going') == (8,21)
    assert longest_subpalindrome_slice('xxxxx') == (0, 5)
    assert longest_subpalindrome_slice('Mad am I ma dam.') == (0, 15)
