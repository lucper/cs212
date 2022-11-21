#!/usr/bin/env python

from regex_compiler import *

def test_lit():
    assert match(lit('hello'), 'hello how are you?') == 'hello'
