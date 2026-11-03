import pytest
from importlib import import_module

lc121_mod = import_module("31_dp_state_machine.0121_best_time_to_buy_and_sell_stock")
lc309_mod = import_module("31_dp_state_machine.0309_best_time_to_buy_and_sell_stock_with_cooldown")


def test_lc121_stock_cases():
    sol = lc121_mod.Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([]) == 0
    assert sol.maxProfit([2, 4, 1]) == 2


def test_lc309_cooldown_cases():
    sol = lc309_mod.Solution()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([1, 4, 2]) == 3
    assert sol.maxProfit([2, 1, 4]) == 3
