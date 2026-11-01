import importlib.util
from pathlib import Path
import pytest

FILE_PATH = Path(__file__).resolve().parent / "0452_minimum_arrows_balloon.py"
spec = importlib.util.spec_from_file_location("arrows_module", FILE_PATH)
arrows_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arrows_module)
Solution = arrows_module.Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([[1, 5]], 1),
        ([], 0),
        ([[-2147483646, -2147483645], [2147483646, 2147483647]], 2),
    ],
)
def test_find_min_arrow_shots(solver, points, expected):
    assert solver.findMinArrowShots(points) == expected
