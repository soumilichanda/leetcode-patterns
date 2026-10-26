import importlib.util
from pathlib import Path
import pytest


def load_module(filename: str):
    file_path = Path(__file__).parent / filename
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


word_ladder_mod = load_module("0127_word_ladder.py")
course_schedule_mod = load_module("0207_course_schedule.py")


def test_word_ladder_standard():
    sol = word_ladder_mod.Solution()
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert sol.ladderLength("hit", "cog", words) == 5


def test_word_ladder_unreachable():
    sol = word_ladder_mod.Solution()
    words = ["hot", "dot", "dog", "lot", "log"]
    assert sol.ladderLength("hit", "cog", words) == 0


def test_word_ladder_end_not_in_list():
    sol = word_ladder_mod.Solution()
    assert sol.ladderLength("hit", "cog", ["hot", "dot"]) == 0


def test_course_schedule_valid_dag():
    sol = course_schedule_mod.Solution()
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True


def test_course_schedule_cycle():
    sol = course_schedule_mod.Solution()
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False


def test_course_schedule_disconnected():
    sol = course_schedule_mod.Solution()
    assert sol.canFinish(3, [[1, 0]]) is True
