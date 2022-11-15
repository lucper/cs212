#!/usr/bin/env python

from regex import *

def test_search_empty_string_vs_emppy_string():
    assert search("", "") == True

def test_search_empty_string_vs_anything():
    assert search("", "bru") == True

def test_search_anyhing_vs_empty_string():
    assert search("^a", "") == False
    assert search("a$", "") == False
    assert search("$", "") == False
    assert search(".", "") == False
    assert search("a", "") == False
    assert search("a?", "") == False
    assert search("a*", "") == False

def test_search_one_char_vs_anything():
    assert search("a", "ab") == True
    assert search("c", "ab") == False

def test_search_two_char_vs_anything():
    assert search("ab", "cabc") == True
    assert search("cc", "abab") == False

def test_matchhere_empty_vs_anything():
    assert match_here("", "") == True
    assert match_here("", "bru") == True

def test_matchhere_anything_vs_empty():
    assert match_here("^a", "") == False
    assert match_here("a$", "") == False
    assert match_here("$", "") == True
    assert match_here(".", "") == False
    assert match_here("a", "") == False
    assert match_here("a?", "") == False
    assert match_here("a*", "") == False

def test_matchhere_dot():
    assert match_here(".", "") == False
    assert match_here(".", "a") == True
    assert match_here(".a", "a") == False
    assert match_here(".a", "ca") == True
    assert match_here(".a.b", "yaxb") == True

def test_matchhere_dollar():
    assert match_here("$", "") == True
    assert match_here("$", "bru") == False
    assert match_here("a$", "") == False
    assert match_here("a$", "ab") == False
    assert match_here("a$", "ba") == True
    assert match_here("a$", "ba cc") == False
