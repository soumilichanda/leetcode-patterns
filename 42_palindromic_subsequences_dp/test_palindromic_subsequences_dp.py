import pytest
from importlib import import_module

lc516 = import_module("42_palindromic_subsequences_dp.0516_longest_palindromic_subsequence").Solution()
lc1312 = import_module("42_palindromic_subsequences_dp.1312_min_insertion_steps_palindrome").Solution()


@pytest.mark.parametrize(
    "s,expected",
    [
        ("bbbab", 4),
        ("cbbd", 2),
        ("a", 1),
        ("ab", 1),
        ("agbdba", 5),
        ("racecar", 7),
    ],
)
def test_longest_palindromic_subsequence(s, expected):
    assert lc516.longestPalindromeSubseq(s) == expected


@pytest.mark.parametrize(
    "s,expected_insertions",
    [
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
        ("g", 0),
        ("no", 1),
    ],
)
def test_min_insertion_steps_palindrome(s, expected_insertions):
    assert lc1312.minInsertions(s) == expected_insertions


def test_lps_duality_invariant():
    samples = ["mbadm", "leetcode", "abacdfgdcaba", "xyz"]
    for s in samples:
        assert lc516.longestPalindromeSubseq(s) + lc1312.minInsertions(s) == len(s)
