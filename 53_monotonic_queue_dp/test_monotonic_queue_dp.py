"""
Parameterized pytest suite for Cluster 53: Monotonic Queue & Deque-Optimized Sliding Window DP.
"""

import importlib.util
from pathlib import Path
import pytest


def _load_solution(filename: str):
    path = Path(__file__).parent / filename
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module.Solution()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([10, 2, -10, 5, 20], 2, 37),
        ([-1, -2, -3], 1, -1),
        ([10, -2, -10, -5, 20], 2, 23),
        ([5], 1, 5),
        ([-5, -2, -8], 3, -2),
    ],
)
def test_lc_1425_constrained_subsequence_sum(nums, k, expected):
    sol = _load_solution("1425_constrained_subsequence_sum.py")
    assert sol.constrainedSubsetSum(nums, k) == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, -1, -2, 4, -7, 3], 2, 7),
        ([10, -5, -2, 4, 0, 3], 3, 17),
        ([1, -5, -20, 4, -1, 3, -6, -3], 2, 0),
        ([42], 1, 42),
    ],
)
def test_lc_1696_jump_game_vi(nums, k, expected):
    sol = _load_solution("1696_jump_game_vi.py")
    assert sol.maxResult(nums, k) == expected
