import pytest
from importlib import import_module

lc124_mod = import_module("36_tree_dp.0124_binary_tree_maximum_path_sum")
lc337_mod = import_module("36_tree_dp.0337_house_robber_iii")

Solution124 = lc124_mod.Solution
Node124 = lc124_mod.TreeNode

Solution337 = lc337_mod.Solution
Node337 = lc337_mod.TreeNode


def test_max_path_sum_all_negatives():
    sol = Solution124()
    tree = Node124(-3, Node124(-2), Node124(-1))
    assert sol.maxPathSum(tree) == -1


def test_max_path_sum_linear_chain():
    sol = Solution124()
    tree = Node124(1, Node124(2, Node124(3)))
    assert sol.maxPathSum(tree) == 6


def test_house_robber_single_node():
    sol = Solution337()
    tree = Node337(42)
    assert sol.rob(tree) == 42


def test_house_robber_balanced_tree():
    sol = Solution337()
    # Tree: [3, 2, 3, None, 3, None, 1]
    tree = Node337(3, Node337(2, None, Node337(3)), Node337(3, None, Node337(1)))
    assert sol.rob(tree) == 7
