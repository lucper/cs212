#!/usr/bin/env python

# Let T be a sequence of chaarcters ("" included).
# We have the following patterns P:
# ""    empty string
# a     first occurrence of character 'a'
# .     first occurrence of a single character, e.g. (".", "abc") => True
# ^a    line beginning with character 'a', e.g. ("^a", "abc") => True
# a?    zero or one occurrence of 'a' in T
# a*    zero or more occurrences of 'a' in T
# a$    line ending with character 'a', e.g. ("a$", "abc") => False
# ab    first occurrence of characters 'a' and 'b' concatenated

def match_here(pattern, text):
    if not pattern:
        return True
    if pattern == '$':
        return not text
    if text and (pattern[0] == text[0] or pattern[0] == '.'):
        return match_here(pattern[1:], text[1:])
    return False

def search(pattern, text):
    if not text:
        return not pattern
    if match_here(pattern, text):
        return True
    return search(pattern, text[1:])
