#!/usr/bin/env python

## API for operators

## See Lesson 3, video 18 ("Simple Compilers"), for some solutions

#dot = ('dot',)
#eol = ('eol',)

def lit(string):
    """ Literal """
    return lambda text: set([text[len(string):]]) if text.startswith(string) else None

def seq(lit1, lit2):
    """ Concatenation """
    pass

def alt(lit1, lit2):
    """ | operator, e.g. 'a|b' matches either 'a' or 'b' """
    pass

def star(lit):
    """ * operator """
    pass

def plus(lit):
    """ + operator """
    pass

def opt(lit):
    """ ? operator """
    pass

def oneof(chars):
    pass

## 

#def matchset(pattern, text):
#    op, x, y = components(pattern)
#    if op == 'lit':
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
