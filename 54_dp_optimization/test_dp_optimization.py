"""
Parameterized pytest suite for Cluster 54: DP Optimization (Interval Median & k-Partitioning).
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
    "houses, k, expected",
    [
        ([1, 4, 8, 10, 20], 3, 5),
        ([2, 3, 5, 12, 18], 2, 9),
        ([7, 4, 6, 1], 1, 8),
        ([3, 6, 14, 10], 4, 0),
        ([10], 1, 0),
    ],
)
def test_lc_1478_allocate_mailboxes(houses, k, expected):
    sol = _load_solution("1478_allocate_mailboxes.py")
    assert sol.minDistance(houses, k) == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([9, 1, 2, 3, 9], 3, 20.0),
        ([1, 2, 3, 4, 5, 6, 7], 4, 20.5),
        ([4, 1, 7, 5, 6, 2, 3], 4, 18.166666666666668),
        ([5], 1, 5.0),
    ],
)
def test_lc_813_largest_sum_of_averages(nums, k, expected):
    sol = _load_solution("0813_largest_sum_of_averages.py")
    assert sol.largestSumOfAverages(nums, k) == pytest.approx(expected, rel=1e-6)
