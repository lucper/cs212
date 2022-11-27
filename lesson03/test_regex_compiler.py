#!/usr/bin/env python

from regex_compiler import *

def test_lit():
    assert match(lit('hello'), 'hello how are you?') == 'hello'

def test_seq_trivial():
    assert match(seq(lit('a'), lit('b')), 'abcd') == 'ab'
    assert match(seq(lit('a'), lit('b')), 'cdab') == None

def test_alt():
    assert match(alt(lit('a'),lit('b')), 'abcd') == 'a'
    assert match(alt(lit('a'),lit('b')), 'bacd') == 'b'
    assert match(alt(lit('a'),lit('b')), 'cdab') == None

def test_star():
    assert match(star(lit('a')), 'aaaaa') == 'aaaaa'
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(star(lit('a')), 'cccccbbbaa') == ''

def test_plus():
    assert match(plus(lit('a')), 'aaaaa') == 'aaaaa'
    assert match(plus(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(plus(lit('a')), 'cccccbbbaa') == None

def test_opt():
    assert match(opt(lit('a')), 'ab') == 'a'
    assert match(opt(lit('a')), 'aaab') == 'a'
    assert match(opt(lit('a')), 'cb') == ''

def test_oneof():
    assert match(oneof('abc'), 'abcer') == 'a'
    assert match(oneof('abc'), 'bbcer') == 'b'
    assert match(oneof('abc'), 'cbcer') == 'c'
    assert match(oneof('abc'), 'xxxer') == None
