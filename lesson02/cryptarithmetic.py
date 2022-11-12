#!/usr/bin/env python

import re
import string
import itertools

def valid(formula):
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False

def fill_in(formula):
    # could be k for k in formula if k in string.ascii_letters
    letters = ''.join(set(re.findall('[a-zA-Z]', formula)))
    for digits in itertools.permutations('0123456789', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def solve(formula):
    # change to print or return list to get all possible assignments
    return next(assign for assign in fill_in(formula) if valid(assign))

### faster approach ###

def compile_word(word):
    # notice that isupper() evaluates to False for characters such as '+' and empty string ''
    return '(' + '+'.join(f'{10**i}*{ch}' for i, ch in enumerate(reversed(word))) + ')' \
            if word.isupper() else word
