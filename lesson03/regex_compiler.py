#!/usr/bin/env python

## API for operators

## See Lesson 3, video 18 ("Simple Compilers"), for some solutions

#dot = ('dot',)
#eol = ('eol',)

def lit(string):
    """ Literal """
    return lambda text: set([text[len(string):]]) if text.startswith(string) else set()

def seq(x, y):
    """ Concatenation """
    return lambda text: set(t2 for t1 in x(text) for t2 in y(t1))

def alt(x, y):
    """ | operator, e.g. 'a|b' matches either 'a' or 'b' """
    return lambda text: x(text) | y(text)

def star(x):
    """ * operator 
    Notice that we make the union with the whole text
    because it is always the remainder of itself.
    In addition, calling star(x) returns the lambda;
    this is how we can recur."""
    return lambda text: set([text]) | set(t2 for t1 in x(text) for t2 in star(x)(t1))

def plus(x):
    """ + operator """
    return lambda text: set(t2 for t1 in x(text) for t2 in star(x)(t1))

def opt(x):
    """ ? operator """
    pass

def oneof(chars):
    return lambda text: set([text[1:]]) if text and text[0] in chars else set()

## 

#def matchset(pattern, text):
#    op, x, y = components(pattern)
#    if op == 'x':
#        return set([text[len(x):]]) if text.startswith(x) else frozenset()
#    elif op == 'seq':
#        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
#    elif op == 'alt':
#        return matchset(x, text) | matchset(y, text)
#    elif op == 'dot':
#        return set([text[1:]]) if text else None
#    elif op == 'oneof':
#        return set([text[1:]]) if text.startswith(x) else None
#    elif op == 'eol':
#        return set(['']) if not text else None
#    elif op == 'star':
#        # !!!
#        return set([text]) | set(t2 for t1 in matchset(x, text) for t2 in matchset(pattern, t1) if t1 != text)
#    else:
#        raise ValueError(f'unknown pattern: {pattern}')

def match(pattern, text):
    """Match pattern against start of text; return longest if found or None otherwise.
    Notice that here the pattern is already "compiled"; we hard coded the corresponding
    functions above. We could, however, write a function that compiles a pattern to its
    function representation, but for this particular problem, there was no need for this
    approach."""
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text)-len(shortest)]

def search(pattern, text):
    for i in range(len(text)):
        if m := match(pattern, text[i:]):
            return m
