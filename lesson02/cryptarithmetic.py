#!/usr/bin/env python

import re

def valid(formula):
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False
