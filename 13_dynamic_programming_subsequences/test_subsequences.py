import pytest
from importlib import import_module

lis_module = import_module("13_dynamic_programming_subsequences.0300_longest_increasing_subsequence")
partition_module = import_module("13_dynamic_programming_subsequences.0416_partition_equal_subset_sum")

SolutionLIS = lis_module.Solution
SolutionPartition = partition_module.Solution


def test_longest_increasing_subsequence():
    sol = SolutionLIS()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert sol.lengthOfLIS([]) == 0


def test_partition_equal_subset_sum():
    sol = SolutionPartition()
    assert sol.canPartition([1, 5, 11, 5]) is True
    assert sol.canPartition([1, 2, 3, 5]) is False
    assert sol.canPartition([1, 2, 5]) is False
