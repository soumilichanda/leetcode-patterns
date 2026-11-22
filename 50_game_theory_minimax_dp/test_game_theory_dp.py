"""Parameterized test suite for Cluster 50: Game Theory & Minimax Optimal Play DP."""

import importlib.util
from pathlib import Path
import pytest

CLUSTER_DIR = Path(__file__).resolve().parent


def _load_solution(filename: str):
    module_path = CLUSTER_DIR / filename
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module.Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 5, 2], False),
        ([1, 5, 233, 7], True),
        ([0], True),
        ([2, 4, 55, 6, 8], False),
        ([1, 1], True),
    ],
)
def test_predict_the_winner(nums, expected):
    sol = _load_solution("0486_predict_the_winner.py")
    assert sol.predictTheWinner(nums) is expected


@pytest.mark.parametrize(
    "piles",
    [
        [5, 3, 4, 5],
        [3, 7, 2, 3],
        [1, 100, 3, 2],
        [7, 8, 8, 10],
    ],
)
def test_stone_game(piles):
    sol = _load_solution("0877_stone_game.py")
    assert sol.stoneGame(piles) is True
