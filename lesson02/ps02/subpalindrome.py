#!/usr/bin/env python

def palindrome(text):
    # O(len(text))
    if not text: 
        return True
    return text[0].upper() == text[len(text)-1].upper() if palindrome(text[1:len(text)-1]) else False

def longest_subpalindrome_slice(text):
    n = len(text)
    if n == 0:
        return 0, 0
    else:
        i, j = longest_subpalindrome_slice(text[:n-1])
        for k in range(n):
            if palindrome(text[k:n]) and j - i < n - k:
                return k, n
        return i, j

def faster_longest_subpalindrome_slice(text):
    n = len(text)
    if n == 0:
        return 0, 0
    elif n == 1:
        return 0, 1
    else:
        mid = n // 2
        i, j = faster_longest_subpalindrome_slice(text[:mid])
        k, l = faster_longest_subpalindrome_slice(text[mid:])
        # overlap case
        p, q = mid-1, mid
        while text[p] == text[q] and q < n and p > -1:
            p -= 1
            q += 1
        if text[p] == text[q]:
            return max([(i, j), (k+len(text[:mid]), l+len(text[:mid])), (p, q+len(text[:mid]))], key=lambda tup: tup[1]-tup[0])
        else:
            return max([(i, j), (k+len(text[:mid]), l+len(text[:mid]))], key=lambda tup: tup[1]-tup[0])
