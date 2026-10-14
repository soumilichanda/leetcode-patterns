from importlib import import_module

mod_53 = import_module("14_greedy.0053_maximum_subarray")
mod_55 = import_module("14_greedy.0055_jump_game")

Solution53 = mod_53.Solution
Solution55 = mod_55.Solution


def test_max_subarray_mixed():
    sol = Solution53()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_single_element():
    sol = Solution53()
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([-7]) == -7


def test_max_subarray_all_negative():
    sol = Solution53()
    assert sol.maxSubArray([-5, -2, -8, -1, -4]) == -1


def test_jump_game_reachable():
    sol = Solution55()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([0]) is True
    assert sol.canJump([2, 0, 0]) is True


def test_jump_game_unreachable_zero_trap():
    sol = Solution55()
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0, 2, 3]) is False
