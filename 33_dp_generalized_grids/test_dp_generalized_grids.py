import pytest
from importlib import import_module

lc188_mod = import_module("33_dp_generalized_grids.0188_best_time_to_buy_and_sell_stock_iv")
lc62_mod = import_module("33_dp_generalized_grids.0062_unique_paths")


def test_lc188_generalized_k():
    sol = lc188_mod.Solution()
    assert sol.maxProfit(2, [2, 4, 1]) == 2
    assert sol.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    assert sol.maxProfit(0, [1, 2, 3]) == 0
    assert sol.maxProfit(1, []) == 0


def test_lc62_unique_paths():
    sol = lc62_mod.Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
