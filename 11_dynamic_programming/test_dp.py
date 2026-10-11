import pytest
from importlib import import_module

climb_mod = import_module("11_dynamic_programming.0070_climbing_stairs")
rob_mod = import_module("11_dynamic_programming.0198_house_robber")


def test_climbing_stairs_cases():
    sol = climb_mod.Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(4) == 5
    assert sol.climbStairs(6) == 13


def test_house_robber_cases():
    sol = rob_mod.Solution()
    assert sol.rob([0]) == 0
    assert sol.rob([2, 1, 1, 2]) == 4
    assert sol.rob([5, 3, 4, 11, 2]) == 16
