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
