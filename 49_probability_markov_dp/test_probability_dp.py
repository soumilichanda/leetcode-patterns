import importlib.util
from pathlib import Path
import pytest

CLUSTER_DIR = Path(__file__).resolve().parent


def _load_solution(filename: str):
    spec = importlib.util.spec_from_file_location(filename, CLUSTER_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()


@pytest.mark.parametrize(
    ("n", "k", "max_pts", "expected"),
    [
        (10, 1, 10, 1.0),
        (6, 1, 10, 0.6),
        (21, 17, 10, 0.73278),
        (0, 0, 1, 1.0),
    ],
)
def test_new_21_game(n: int, k: int, max_pts: int, expected: float) -> None:
    sol = _load_solution("0837_new_21_game.py")
    assert sol.new21Game(n, k, max_pts) == pytest.approx(expected, abs=1e-5)


@pytest.mark.parametrize(
    ("n", "k", "row", "col", "expected"),
    [
        (3, 2, 0, 0, 0.0625),
        (1, 0, 0, 0, 1.0),
        (8, 30, 6, 4, 0.00019),
    ],
)
def test_knight_probability(n: int, k: int, row: int, col: int, expected: float) -> None:
    sol = _load_solution("0688_knight_probability_in_chessboard.py")
    assert sol.knightProbability(n, k, row, col) == pytest.approx(expected, abs=1e-5)
