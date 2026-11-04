import pytest
from importlib import import_module

lc714_mod = import_module("32_dp_multidimensional_stock.0714_best_time_to_buy_and_sell_stock_with_transaction_fee")
lc123_mod = import_module("32_dp_multidimensional_stock.0123_best_time_to_buy_and_sell_stock_iii")


def test_lc714_transaction_fee():
    sol = lc714_mod.Solution()
    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
    assert sol.maxProfit([1, 4], 5) == 0
    assert sol.maxProfit([], 2) == 0


def test_lc123_two_transactions():
    sol = lc123_mod.Solution()
    assert sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([2, 1, 2, 0, 1]) == 2
