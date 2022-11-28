#!/usr/bin/env python

import re

def grammar(description, whitespace=r"\s*"):
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs
    for line in description.strip().split("\n"):
        lhs, rhs = [x.strip() for x in line.split(" => ")]
        alternatives = rhs.split(" | ")
        G[lhs] = tuple(alt.split() for alt in alternatives)
    return G

def parse(start_symbol, text, grammar):
    tokenizer = grammar[' '] + '({})' # !!!

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if not text:
                return None, None
            result.append(tree)
        return result, text

    def parse_atom(atom, text):
        if atom in grammar:
            for alt in grammar[atom]:
                tree, rem = parse_sequence(alt, text)
                if not rem:
                    return [atom] + tree, rem
                return None, None
        else:
            m = re.match(tokenizer.format(atom), text)
            return (None, None) if not m else (m.group(1), text[m.end():])

    return parse_atom(start_symbol, text)

G = grammar(r"""
Exp     => Term [+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [+-]?[0-9]+([.][0-9]*)?
""")

print(G)
