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
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (13, 6),
        (100, 21),
        (824883294, 767944060),
    ],
)
def test_count_digit_one(n: int, expected: int) -> None:
    sol = _load_solution("0233_number_of_digit_one.py")
    assert sol.countDigitOne(n) == expected


@pytest.mark.parametrize(
    ("digits", "n", "expected"),
    [
        (["1", "3", "5", "7"], 100, 20),
        (["1", "4", "9"], 1000000000, 29523),
        (["7"], 8, 1),
        (["3", "4", "8"], 4, 2),
    ],
)
def test_at_most_n_given_digit_set(digits: list[str], n: int, expected: int) -> None:
    sol = _load_solution("0902_numbers_at_most_n_given_digit_set.py")
    assert sol.atMostNGivenDigitSet(digits, n) == expected
