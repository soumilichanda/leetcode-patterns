import pytest
from importlib import import_module

trie_mod = import_module("08_tries.0208_implement_trie")
word_dict_mod = import_module("08_tries.0211_design_add_and_search_words")


def test_trie_prefix_operations():
    trie = trie_mod.Trie()
    trie.insert("banana")
    assert trie.search("banana") is True
    assert trie.search("ban") is False
    assert trie.startsWith("ban") is True
    trie.insert("ban")
    assert trie.search("ban") is True


def test_word_dictionary_wildcards():
    wd = word_dict_mod.WordDictionary()
    wd.addWord("code")
    wd.addWord("cold")
    assert wd.search("code") is True
    assert wd.search("co.e") is True
    assert wd.search(".o.e") is True
    assert wd.search("c...") is True
    assert wd.search("c..") is False
