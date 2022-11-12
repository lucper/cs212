#!/usr/bin/env python

import re
import string
import itertools

def compile_word(word):
    # notice that isupper() evaluates to False for characters such as '+' and empty string ''
    return '(' + '+'.join(f'{10**i}*{ch}' for i, ch in enumerate(reversed(word))) + ')' \
            if word.isupper() else word

def compile_formula(formula, verbose=False):
    # compiles a formula into a anonymous function
    # e.g. AB+CB==AC => lambda A, B, C: (1*B + 10*A) + (1*B + 10*C) == (1*C + 10*A)

    # construct parameters of lambda
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    first_letters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    params = ', '.join(letters)

    # construct body of lambda
    ## capturing parentheses makes pattern to be returned
    ## ex. 'e+r=a' => ['', 'e', '+', 'r', '=', 'a', '']
    ## instead of 'e+r=a' => ['', '+', '=', '']
    body = ''.join(compile_word(word) for word in re.split(r'([A-Z]+)', formula))
    if first_letters:
        tests = ' and '.join(f'{letter}!=0' for letter in first_letters)
        body = f'{tests} and ({body})'

    fn = f'(lambda {params}: {body})'
    if verbose:
        print(fn)
    return eval(fn), letters

def faster_solve(formula):
    fn, letters = compile_formula(formula)
    for digits in itertools.permutations(range(10), len(letters)):
        try:
            if fn(*digits):
                table = str.maketrans(letters, ''.join(str(i) for i in digits))
                return formula.translate(table)
        except ArithmeticError:
                pass
