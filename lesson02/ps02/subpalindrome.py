#!/usr/bin/env python

def palindrome(text):
    # O(len(text))
    if not text: 
        return True
    return text[0].upper() == text[len(text)-1].upper() if palindrome(text[1:len(text)-1]) else False

def longest_subpalindrome_slice(text):
    print(text)
    n = len(text)
    if n == 0:
        return 0, 0
    else:
        i, j = longest_subpalindrome_slice(text[:n-1])
        for k in range(n):
            if palindrome(text[k:n]) and j - i < n - k:
                return k, n
        return i, j
