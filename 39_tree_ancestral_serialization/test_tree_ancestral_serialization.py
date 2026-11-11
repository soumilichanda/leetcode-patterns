import pytest
from importlib import import_module

lc236_mod = import_module("39_tree_ancestral_serialization.0236_lowest_common_ancestor")
lc297_mod = import_module("39_tree_ancestral_serialization.0297_serialize_and_deserialize_binary_tree")

Solution236 = lc236_mod.Solution
TreeNode236 = lc236_mod.TreeNode

Codec297 = lc297_mod.Codec
TreeNode297 = lc297_mod.TreeNode


def test_lca_direct_parent_child():
    sol = Solution236()
    child = TreeNode236(2)
    root = TreeNode236(1, child, None)
    assert sol.lowestCommonAncestor(root, root, child) == root


def test_lca_disjoint_branches():
    sol = Solution236()
    p = TreeNode236(4)
    q = TreeNode236(5)
    root = TreeNode236(1, TreeNode236(2, p, None), TreeNode236(3, None, q))
    assert sol.lowestCommonAncestor(root, p, q) == root


def test_serialize_deserialize_empty():
    codec = Codec297()
    serialized = codec.serialize(None)
    assert serialized == "#"
    assert codec.deserialize(serialized) is None


def test_serialize_deserialize_linear_chain():
    codec = Codec297()
    # 1 -> 2 -> 3
    root = TreeNode297(1, TreeNode297(2, TreeNode297(3), None), None)
    data = codec.serialize(root)
    recovered = codec.deserialize(data)
    assert codec.serialize(recovered) == data
