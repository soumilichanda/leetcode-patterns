import pytest
from importlib import import_module

lc5 = import_module("34_palindromic_substrings.0005_longest_palindromic_substring").Solution()
lc647 = import_module("34_palindromic_substrings.0647_palindromic_substrings").Solution()


@pytest.mark.parametrize(
    "s,expected_options",
    [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("racecar", ["racecar"]),
        ("ac", ["a", "c"]),
    ],
)
def test_longest_palindrome(s, expected_options):
    res = lc5.longestPalindrome(s)
    assert res in expected_options


@pytest.mark.parametrize(
    "s,expected_count",
    [
        ("abc", 3),
        ("aaa", 6),
        ("racecar", 10),
        ("noon", 6),
        ("x", 1),
    ],
)
def test_count_substrings(s, expected_count):
    assert lc647.countSubstrings(s) == expected_count
