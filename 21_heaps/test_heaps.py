import pytest
from importlib import import_module

lc215_mod = import_module("21_heaps.0215_kth_largest_element")
lc295_mod = import_module("21_heaps.0295_find_median_from_data_stream")


def test_kth_largest_basic():
    sol = lc215_mod.Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_kth_largest_duplicates_and_negatives():
    sol = lc215_mod.Solution()
    assert sol.findKthLargest([-1, -1, 2], 1) == 2
    assert sol.findKthLargest([7, 7, 7, 7], 2) == 7


def test_median_finder_streaming():
    mf = lc295_mod.MedianFinder()
    mf.addNum(6)
    assert mf.findMedian() == 6.0
    mf.addNum(10)
    assert mf.findMedian() == 8.0
    mf.addNum(2)
    assert mf.findMedian() == 6.0
    mf.addNum(6)
    assert mf.findMedian() == 6.0
    mf.addNum(5)
    assert mf.findMedian() == 6.0
