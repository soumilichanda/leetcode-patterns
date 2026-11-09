import pytest
from importlib import import_module

lc543_mod = import_module("37_tree_rerooting_diameter.0543_diameter_of_binary_tree")
lc834_mod = import_module("37_tree_rerooting_diameter.0834_sum_of_distances_in_tree")

Solution543 = lc543_mod.Solution
TreeNode543 = lc543_mod.TreeNode
Solution834 = lc834_mod.Solution


def test_diameter_linear_tree():
    sol = Solution543()
    root = TreeNode543(1, TreeNode543(2, TreeNode543(3, TreeNode543(4))))
    assert sol.diameterOfBinaryTree(root) == 3


def test_diameter_symmetric():
    sol = Solution543()
    root = TreeNode543(1, TreeNode543(2), TreeNode543(3))
    assert sol.diameterOfBinaryTree(root) == 2


def test_sum_of_distances_star_graph():
    sol = Solution834()
    out = sol.sumOfDistancesInTree(4, [[0, 1], [0, 2], [0, 3]])
    assert out == [3, 5, 5, 5]


def test_sum_of_distances_single_node():
    sol = Solution834()
    assert sol.sumOfDistancesInTree(1, []) == [0]
