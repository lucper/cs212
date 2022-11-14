#!/usr/bin/env python

def palindrome(text):
    # O(len(text))
    if not text: 
        return True
    return text[0].upper() == text[len(text)-1].upper() if palindrome(text[1:len(text)-1]) else False

def longest_palindrome_slice(text):
    n = len(text)
    if n == 0:
        return 0, 0
    else:
        i, j = longest_palindrome_slice(text[:n-1])
        for k in range(n):
            if palindrome(text[k:n]) and j - i < n - k:
                return k, n
        return i, j

def faster_longest_palindrome_slice(text):
    if not text:
        return 0, 0

    n = len(text)
    memo = [[False for j in range(n)] for i in range(n)]

    for i in range(n):
        memo[i][i] = True

    for i in range(n-1):
        if text[i].upper() == text[i+1].upper():
            memo[i][i+1] = True

    for i in range(n-3, -1, -1):
        for j in range(i+1, n):
            if text[i].upper() == text[j].upper():
                memo[i][j] = memo[i+1][j-1]

    longest_length, k, l = 1, 0, 0
    for i in range(n):
        for j in range(i+1, n):
            if memo[i][j] and j - i + 1 > longest_length:
                longest_length, k, l = j - i + 1, i, j
    
    return k, l+1

