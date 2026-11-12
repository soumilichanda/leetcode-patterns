import pytest
from importlib import import_module

lc96_mod = import_module("40_catalan_bst_dp.0096_unique_binary_search_trees")
lc95_mod = import_module("40_catalan_bst_dp.0095_unique_binary_search_trees_ii")

Solution96 = lc96_mod.Solution
Solution95 = lc95_mod.Solution


def inorder_vals(root):
    if not root:
        return []
    return inorder_vals(root.left) + [root.val] + inorder_vals(root.right)


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 14),
        (5, 42),
    ],
)
def test_catalan_counts(n, expected):
    sol = Solution96()
    assert sol.numTrees(n) == expected


def test_generate_trees_invariants():
    sol = Solution95()
    trees = sol.generateTrees(3)
    assert len(trees) == 5
    for tree in trees:
        assert inorder_vals(tree) == [1, 2, 3]
