import pytest
from 20_tries.0212_word_search_ii import Solution


def test_word_search_ii_basic():
    sol = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(sol.findWords(board, words)) == sorted(["eat", "oath"])


def test_word_search_ii_no_match():
    sol = Solution()
    board = [["a", "b"], ["c", "d"]]
    words = ["abcd", "efg"]
    assert sol.findWords(board, words) == []


def test_word_search_ii_prefix_reuse():
    sol = Solution()
    board = [["a", "b"], ["a", "a"]]
    words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
    res = sol.findWords(board, words)
    assert "aaa" in res
    assert "aba" in res
