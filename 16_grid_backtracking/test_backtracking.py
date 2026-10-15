import pytest
from importlib import import_module

perm_mod = import_module("16_grid_backtracking.0046_permutations")
word_mod = import_module("16_grid_backtracking.0079_word_search")


def test_permutations_cardinality():
    sol = perm_mod.Solution()
    res = sol.permute([1, 2, 3])
    assert len(res) == 6
    assert [1, 2, 3] in res
    assert [3, 2, 1] in res


def test_word_search_grid():
    sol = word_mod.Solution()
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    assert sol.exist(board, "ABCCED") is True
    assert sol.exist(board, "SEE") is True
    assert sol.exist(board, "ABCB") is False
