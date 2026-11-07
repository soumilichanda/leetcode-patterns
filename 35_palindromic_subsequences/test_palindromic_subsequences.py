import pytest
from importlib import import_module

lc516 = import_module("35_palindromic_subsequences.0516_longest_palindromic_subsequence").Solution()
lc132 = import_module("35_palindromic_subsequences.0132_palindrome_partitioning_ii").Solution()


@pytest.mark.parametrize(
    "s,expected",
    [
        ("bbbab", 4),
        ("cbbd", 2),
        ("a", 1),
        ("agbdba", 5),
    ],
)
def test_longest_palindrome_subseq(s, expected):
    assert lc516.longestPalindromeSubseq(s) == expected


@pytest.mark.parametrize(
    "s,expected_cuts",
    [
        ("aab", 1),
        ("a", 0),
        ("ab", 1),
        ("abacaba", 0),
        ("coder", 4),
    ],
)
def test_palindrome_partitioning_min_cuts(s, expected_cuts):
    assert lc132.minCut(s) == expected_cuts
