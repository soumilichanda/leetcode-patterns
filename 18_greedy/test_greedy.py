import importlib.util
from pathlib import Path

def load_module_from_file(file_path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

base_dir = Path(__file__).resolve().parent
jump1_mod = load_module_from_file(str(base_dir / "0055_jump_game.py"), "jump1_mod")
jump2_mod = load_module_from_file(str(base_dir / "0045_jump_game_ii.py"), "jump2_mod")


def test_can_jump_cases():
    sol = jump1_mod.Solution()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0]) is True


def test_jump_ii_cases():
    sol = jump2_mod.Solution()
    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
    assert sol.jump([0]) == 0
