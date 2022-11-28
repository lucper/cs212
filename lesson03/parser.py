#!/usr/bin/env python

# keys are left with wite spaces
def grammar(description):
    G = {}
    for line in description.strip().split("\n"):
        lhs, rhs = line.split("=>")
        alternatives = rhs.split("|")
        G[lhs] = tuple(alt.split() for alt in alternatives)
    return G

# does not admit white spaces
G = grammar(r"""
Exp     => Term [+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [+-]?[0-9]+([.][0-9]*)?
""")
