import pytest
from importlib import import_module

lc_684 = import_module("24_mst_union_find.0684_redundant_connection")
lc_1584 = import_module("24_mst_union_find.1584_min_cost_to_connect_all_points")


def test_lc_684_redundant_connection_triangle():
    sol = lc_684.Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    assert sol.findRedundantConnection(edges) == [2, 3]


def test_lc_684_redundant_connection_cycle_in_component():
    sol = lc_684.Solution()
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert sol.findRedundantConnection(edges) == [1, 4]


def test_lc_1584_min_cost_square():
    sol = lc_1584.Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert sol.minCostConnectPoints(points) == 20


def test_lc_1584_min_cost_triangle():
    sol = lc_1584.Solution()
    points = [[3, 12], [-2, 5], [-4, 1]]
    assert sol.minCostConnectPoints(points) == 18
