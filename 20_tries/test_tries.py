import pytest
from importlib import import_module

trie_mod = import_module("20_tries.0208_implement_trie")
word_dict_mod = import_module("20_tries.0211_design_add_and_search_words")


def test_trie_invariants():
    trie = trie_mod.Trie()
    trie.insert("flower")
    trie.insert("flow")
    assert trie.search("flow") is True
    assert trie.search("flight") is False
    assert trie.startsWith("f") is True
    assert trie.startsWith("flo") is True


def test_word_dict_wildcard_backtracking():
    wd = word_dict_mod.WordDictionary()
    wd.addWord("system")
    wd.addWord("syntax")
    assert wd.search("sys..") is False    # 5 chars vs 6 chars -> False
    assert wd.search("sys...") is True    # matches 'system' (6 chars)
    assert wd.search("sys.em") is True    # matches 'system'
    assert wd.search("s.....") is True    # matches 'system' / 'syntax'
    assert wd.search("......") is True    # matches 6-letter word
