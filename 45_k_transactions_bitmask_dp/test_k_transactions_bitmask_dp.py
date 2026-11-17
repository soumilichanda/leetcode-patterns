from importlib import import_module

lc188_mod = import_module("45_k_transactions_bitmask_dp.0188_best_time_to_buy_and_sell_stock_iv")
lc1986_mod = import_module("45_k_transactions_bitmask_dp.1986_min_work_sessions")


def test_lc188_stock_iv():
    sol = lc188_mod.Solution()
    assert sol.maxProfit(2, [2, 4, 1]) == 2
    assert sol.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    assert sol.maxProfit(0, [1, 5, 9]) == 0
    assert sol.maxProfit(100, [1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit(2, [7, 6, 4, 3, 1]) == 0


def test_lc1986_min_work_sessions():
    sol = lc1986_mod.Solution()
    assert sol.minSessions([1, 2, 3], 3) == 2
    assert sol.minSessions([3, 1, 3, 1, 1], 8) == 2
    assert sol.minSessions([1, 2, 3, 4, 5], 15) == 1
    assert sol.minSessions([9, 8, 8, 4, 6], 14) == 3
