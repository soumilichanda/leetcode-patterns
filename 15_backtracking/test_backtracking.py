from importlib import import_module

mod_78 = import_module("15_backtracking.0078_subsets")
mod_39 = import_module("15_backtracking.0039_combination_sum")

Solution78 = mod_78.Solution
Solution39 = mod_39.Solution


def test_subsets_power_set_size():
    sol = Solution78()
    res = sol.subsets([1, 2, 3])
    assert len(res) == 8
    assert [] in res
    assert [1, 2, 3] in res


def test_subsets_empty_and_single():
    sol = Solution78()
    assert sol.subsets([]) == [[]]
    assert sol.subsets([0]) == [[], [0]]


def test_combination_sum_target():
    sol = Solution39()
    res = sol.combinationSum([2, 3, 6, 7], 7)
    assert sorted(res) == sorted([[2, 2, 3], [7]])


def test_combination_sum_no_match():
    sol = Solution39()
    assert sol.combinationSum([2], 1) == []
