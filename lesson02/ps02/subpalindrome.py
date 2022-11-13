#!/usr/bin/env python

def palindrome(text):
    # O(len(text))
    if not text: 
        return True
    return text[0] == text[len(text)-1] if palindrome(text[1:len(text)-1]) else False

def longest_subpalindrome_slice(text):
    print(text)
    if not text:
        return 0, 0
    elif len(text) == 1:
        return 0, 0
    else:
        mid = len(text) // 2
        i, j = longest_subpalindrome_slice(text[:mid])
        k, l = longest_subpalindrome_slice(text[mid:])
        # text[:mid][-1] == text[:mid][0]
        # text[:mid][-2] == text[:mid][1]
        # text[:mid][-3] == text[:mid][2]
        # and so on
        x, y = -1, 0
        while text[:mid][x] == text[mid:][y]:
            x -= 1
            y += 1
        x = mid - x
        return max([(i,j), (k,l), (x,y)], key=lambda tup: tup[1]-tup[0])
