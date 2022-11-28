#!/usr/bin/env python

def grammar(description, whitespace=r"\s*"):
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs
    for line in description.strip().split("\n"):
        lhs, rhs = [x.strip() for x in line.split(" => ")]
        alternatives = rhs.split(" | ")
        G[lhs] = tuple(alt.split() for alt in alternatives)
    return G

def parse(start_symbol, text, grammar):
    pass

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
