import importlib.util
from pathlib import Path
import pytest


def _load_module(relative_path: str):
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / relative_path
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sol322_mod = _load_module("0322_coin_change.py")
sol518_mod = _load_module("0518_coin_change_ii.py")


def test_coin_change_reachable():
    sol = sol322_mod.Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2, 5, 10, 1], 27) == 4


def test_coin_change_unreachable_and_zero():
    sol = sol322_mod.Solution()
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0


def test_coin_change_ii_combinations():
    sol = sol518_mod.Solution()
    assert sol.change(5, [1, 2, 5]) == 4
    assert sol.change(3, [2]) == 0
    assert sol.change(10, [10]) == 1
    assert sol.change(0, [7]) == 1
