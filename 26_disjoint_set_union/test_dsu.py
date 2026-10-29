from importlib import import_module

lc_684 = import_module("26_disjoint_set_union.0684_redundant_connection")
lc_547 = import_module("26_disjoint_set_union.0547_number_of_provinces")


def test_lc_684_simple_cycle():
    sol = lc_684.Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    assert sol.findRedundantConnection(edges) == [2, 3]


def test_lc_684_extended_cycle():
    sol = lc_684.Solution()
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert sol.findRedundantConnection(edges) == [1, 4]


def test_lc_547_two_provinces():
    sol = lc_547.Solution()
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert sol.findCircleNum(is_connected) == 2


def test_lc_547_isolated_provinces():
    sol = lc_547.Solution()
    is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert sol.findCircleNum(is_connected) == 3


def test_lc_547_single_component():
    sol = lc_547.Solution()
    is_connected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert sol.findCircleNum(is_connected) == 1
