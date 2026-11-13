import importlib.util
from pathlib import Path
import pytest

BASE_DIR = Path(__file__).resolve().parent


def _load_solution(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([7], 7),
        ([0, 0, 0], 0),
        ([9, 76, 64, 21], 116718),
    ],
)
def test_burst_balloons(nums, expected):
    solver = _load_solution("0312_burst_balloons.py", "lc312")
    assert solver.maxCoins(nums) == expected


@pytest.mark.parametrize(
    "n, cuts, expected",
    [
        (7, [1, 3, 4, 5], 16),
        (9, [5, 6, 1, 4, 2], 22),
        (10, [5], 10),
        (20, [2, 8, 12, 17], 48),
    ],
)
def test_min_cost_cut_stick(n, cuts, expected):
    solver = _load_solution("1547_minimum_cost_to_cut_a_stick.py", "lc1547")
    assert solver.minCost(n, cuts) == expected
