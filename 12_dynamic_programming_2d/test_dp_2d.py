import pytest
from importlib import import_module

paths_mod = import_module("12_dynamic_programming_2d.0062_unique_paths")
lcs_mod = import_module("12_dynamic_programming_2d.1143_longest_common_subsequence")


def test_unique_paths():
    sol = paths_mod.Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 3) == 6
    assert sol.uniquePaths(7, 3) == 28


def test_longest_common_subsequence():
    sol = lcs_mod.Solution()
    assert sol.longestCommonSubsequence("abcba", "abcbcba") == 5
    assert sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert sol.longestCommonSubsequence("", "a") == 0
