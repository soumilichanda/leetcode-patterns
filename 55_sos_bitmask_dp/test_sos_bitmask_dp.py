"""Parameterized test suite for Cluster 55: Sum Over Subsets (SOS) & Bitwise Convolution DP."""

import importlib.util
from pathlib import Path
import pytest

CLUSTER_DIR = Path(__file__).resolve().parent


def _load_solution(filename: str):
    module_path = CLUSTER_DIR / filename
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module.Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 1, 3], 12),
        ([0, 0, 0], 27),
        ([1, 2, 4, 8], 60),
        ([7, 7, 7], 0),
        ([0, 1], 7),
    ],
)
def test_triples_with_bitwise_and_zero(nums, expected):
    sol = _load_solution("0982_triples_with_bitwise_and_equal_to_zero.py")
    assert sol.countTriplets(list(nums)) == expected


@pytest.mark.parametrize(
    "words,puzzles,expected",
    [
        (
            ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
            ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"],
            [1, 1, 3, 2, 4, 0],
        ),
        (
            ["apple", "pleas", "please"],
            ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"],
            [0, 1, 3, 2, 0],
        ),
        (
            ["abcdefgh"],  # 8 distinct letters -> cannot match any 7-char puzzle
            ["abcdefg"],
            [0],
        ),
    ],
)
def test_number_of_valid_words_for_each_puzzle(words, puzzles, expected):
    sol = _load_solution("1178_number_of_valid_words_for_each_puzzle.py")
    assert sol.findNumOfValidWords(words, puzzles) == expected
