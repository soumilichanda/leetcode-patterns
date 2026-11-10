import pytest
from importlib import import_module

lc968_mod = import_module("38_tree_ancestral_dp.0968_binary_tree_cameras")
lc687_mod = import_module("38_tree_ancestral_dp.0687_longest_univalue_path")

Solution968 = lc968_mod.Solution
TreeNode968 = lc968_mod.TreeNode

Solution687 = lc687_mod.Solution
TreeNode687 = lc687_mod.TreeNode


def test_cameras_single_node():
    sol = Solution968()
    root = TreeNode968(0)
    assert sol.minCameraCover(root) == 1


def test_cameras_balanced_tree():
    sol = Solution968()
    # 0 -> (0, 0)
    root = TreeNode968(0, TreeNode968(0), TreeNode968(0))
    assert sol.minCameraCover(root) == 1


def test_cameras_vertical_chain():
    sol = Solution968()
    # 0 -> 0 -> 0
    root = TreeNode968(0, TreeNode968(0, TreeNode968(0)))
    assert sol.minCameraCover(root) == 1


def test_univalue_all_same_values():
    sol = Solution687()
    # Tree where all values are 1, depth 2, path length 2
    root = TreeNode687(1, TreeNode687(1), TreeNode687(1))
    assert sol.longestUnivaluePath(root) == 2


def test_univalue_empty_and_single():
    sol = Solution687()
    assert sol.longestUnivaluePath(None) == 0
    assert sol.longestUnivaluePath(TreeNode687(42)) == 0


def test_univalue_forked_mismatch():
    sol = Solution687()
    # Root 1 has children with val 2 and 3
    root = TreeNode687(1, TreeNode687(2), TreeNode687(3))
    assert sol.longestUnivaluePath(root) == 0
