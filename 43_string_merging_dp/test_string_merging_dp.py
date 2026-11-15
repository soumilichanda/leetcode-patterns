import pytest
from importlib import import_module

lc97 = import_module("43_string_merging_dp.0097_interleaving_string").Solution()
lc115 = import_module("43_string_merging_dp.0115_distinct_subsequences").Solution()


@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
        ("", "abc", "abc", True),
        ("abc", "", "abd", False),
        ("ab", "bc", "babc", True),
    ],
)
def test_interleaving_string(s1, s2, s3, expected):
    assert lc97.isInterleave(s1, s2, s3) == expected


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
        ("aaa", "a", 3),
        ("aaa", "aa", 3),
        ("abc", "abcd", 0),
        ("abc", "", 1),
    ],
)
def test_distinct_subsequences(s, t, expected):
    assert lc115.numDistinct(s, t) == expected
