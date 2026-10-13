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
import pytest
from importlib import import_module

lis_module = import_module("13_dynamic_programming_subsequences.0300_longest_increasing_subsequence")
partition_module = import_module("13_dynamic_programming_subsequences.0416_partition_equal_subset_sum")

SolutionLIS = lis_module.Solution
SolutionPartition = partition_module.Solution


def test_longest_increasing_subsequence_edge_cases():
    sol = SolutionLIS()
    # Decreasing array: each subsequence length is 1
    assert sol.lengthOfLIS([9, 8, 7, 6, 5]) == 1
    # Strictly increasing array
    assert sol.lengthOfLIS([1, 2, 3, 4, 5]) == 5
    # Single element
    assert sol.lengthOfLIS([42]) == 1


def test_partition_equal_subset_sum_edge_cases():
    sol = SolutionPartition()
    # Odd sum immediately returns False
    assert sol.canPartition([1, 2, 4]) is False
    # Identical elements
    assert sol.canPartition([5, 5]) is True
    # Single element cannot be partitioned
    assert sol.canPartition([10]) is False
