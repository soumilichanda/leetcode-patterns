import pytest
from importlib import import_module

islands_mod = import_module("22_graphs.0200_number_of_islands")
clone_mod = import_module("22_graphs.0133_clone_graph")


def test_number_of_islands_empty_and_single():
    sol = islands_mod.Solution()
    assert sol.numIslands([]) == 0
    assert sol.numIslands([["0"]]) == 0
    assert sol.numIslands([["1"]]) == 1


def test_number_of_islands_disconnected():
    sol = islands_mod.Solution()
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"]
    ]
    assert sol.numIslands(grid) == 5


def test_clone_graph_cycle():
    sol = clone_mod.Solution()
    Node = clone_mod.Node
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]

    cloned_root = sol.cloneGraph(n1)
    assert cloned_root is not n1
    assert len(cloned_root.neighbors) == 2
    assert {nb.val for nb in cloned_root.neighbors} == {2, 3}
