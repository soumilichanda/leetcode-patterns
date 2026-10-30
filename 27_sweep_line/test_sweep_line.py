import pytest
from importlib import import_module

lc253_mod = import_module("27_sweep_line.0253_meeting_rooms_ii")
lc57_mod = import_module("27_sweep_line.0057_insert_interval")


@pytest.fixture
def sweep_solver():
    return lc253_mod.Solution()


@pytest.fixture
def insert_solver():
    return lc57_mod.Solution()


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([], 0),
        ([[1, 5]], 1),
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 4], [2, 5], [3, 6]], 3),
        ([[1, 5], [5, 10], [10, 15]], 1),  # Edge contact allowed with no overlap
    ],
)
def test_lc253_min_meeting_rooms(sweep_solver, intervals, expected):
    assert sweep_solver.minMeetingRooms([list(x) for x in intervals]) == expected


@pytest.mark.parametrize(
    "intervals, new_interval, expected",
    [
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        ([[1, 5]], [0, 0], [[0, 0], [[1, 5]]][1:] if False else [[0, 0], [1, 5]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ],
)
def test_lc57_insert_interval(insert_solver, intervals, new_interval, expected):
    assert insert_solver.insert([list(x) for x in intervals], list(new_interval)) == expected
