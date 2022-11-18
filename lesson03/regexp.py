#!/usr/bin/env python

## API for operators

dot = ('dot',)
eol = ('eol',)

def lit(string):
    """ Literal """
    return ('lit', string)

def seq(lit1, lit2):
    """ Concatenation """
    return ('seq', lit1, lit2)

def alt(lit1, lit2):
    """ | operator, e.g. 'a|b' matches either 'a' or 'b' """
    return ('alt', lit1, lit2)

def star(lit):
    """ * operator """
    return ('star', lit)

def plus(lit):
    """
    + operator
    >>> plus(lit('a'))
    >>> ('seq', ('lit', 'a'), ('star', ('lit', 'a')))
    """
    return seq(lit, star(lit))

def opt(lit):
    """ ? operator """
    return alt(lit(''), lit)

def oneof(chars):
    """
    >>> oneof('abc')
    >>> ('oneof', ('a', 'b', 'c'))
    """
    return ('oneof', tuple(chars))

## 

def components(pattern):
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y

def matchset(pattern, text):
    op, x, y = components(pattern)
    if op == 'lit':
        return set([text[len(x):]]) if text.startswith(x) else frozenset()
    elif op == 'seq':
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif op == 'alt':
        return matchset(x, text) | matchset(y, text)
    elif op == 'dot':
        return set([text[1:]]) if text else None
    elif op == 'oneof':
        return set([text[1:]]) if text.startswith(x) else None
    elif op == 'eol':
        return set(['']) if not text else None
    elif op == 'star':
        # !!!
        return set([text]) | set(t2 for t1 in matchset(x, text) for t2 in matchset(pattern, t1) if t1 != text)
    else:
        raise ValueError(f'unknown pattern: {pattern}')

def match(pattern, text):
    """Match pattern against start of text; return longest if found or None otherwise"""
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:-len(shortest)]
