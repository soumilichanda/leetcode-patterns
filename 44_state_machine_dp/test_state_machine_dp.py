from importlib import import_module

lc309_mod = import_module("44_state_machine_dp.0309_stock_with_cooldown")
lc714_mod = import_module("44_state_machine_dp.0714_stock_with_transaction_fee")


def test_lc309_stock_with_cooldown():
    sol = lc309_mod.Solution()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([]) == 0
    assert sol.maxProfit([2, 1, 4]) == 3
    assert sol.maxProfit([6, 1, 3, 2, 4, 7]) == 6


def test_lc714_stock_with_transaction_fee():
    sol = lc714_mod.Solution()
    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
    assert sol.maxProfit([5], 1) == 0
    assert sol.maxProfit([], 2) == 0
    assert sol.maxProfit([4, 5, 2, 4, 3, 3, 1, 2, 5, 4], 1) == 4
