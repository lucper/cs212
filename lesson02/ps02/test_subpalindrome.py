#!/usr/bin/env python

from subpalindrome import *

def test():
    assert faster_longest_palindrome_slice('racecar') == (0, 7)
    assert faster_longest_palindrome_slice('Racecar') == (0, 7)
    assert faster_longest_palindrome_slice('RacecarX') == (0, 7)
    assert faster_longest_palindrome_slice('Race carr') == (7, 9)
    assert faster_longest_palindrome_slice('') == (0, 0)
    assert faster_longest_palindrome_slice('something rac e car going') == (8,21)
    assert faster_longest_palindrome_slice('xxxxx') == (0, 5)
    assert faster_longest_palindrome_slice('Mad am I ma dam.') == (0, 15)
