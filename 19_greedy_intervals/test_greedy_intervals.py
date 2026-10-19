import pytest
from 19_greedy_intervals.0435_non_overlapping_intervals import Solution as S435
from 19_greedy_intervals.0763_partition_labels import Solution as S763


def test_erase_overlap_intervals():
    sol = S435()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([]) == 0
    assert sol.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2


def test_partition_labels():
    sol = S763()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("a") == [1]
