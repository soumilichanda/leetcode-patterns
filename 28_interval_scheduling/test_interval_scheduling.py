import pytest
from importlib import import_module

mod_56 = import_module("28_interval_scheduling.0056_merge_intervals")
mod_435 = import_module("28_interval_scheduling.0435_non_overlapping_intervals")

Solution56 = mod_56.Solution
Solution435 = mod_435.Solution


def test_merge_intervals_overlapping():
    sol = Solution56()
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_merge_intervals_contained():
    sol = Solution56()
    assert sol.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert sol.merge([[1, 10], [2, 3], [4, 5], [6, 7]]) == [[1, 10]]


def test_erase_overlap_intervals():
    sol = Solution435()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
