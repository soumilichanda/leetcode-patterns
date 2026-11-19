import importlib.util
from pathlib import Path
import pytest

CLUSTER_DIR = Path(__file__).parent


def _load_solution(filename: str):
    spec = importlib.util.spec_from_file_location(filename[:-3], CLUSTER_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module.Solution()


@pytest.mark.parametrize(
    "n,edges,expected",
    [
        (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]], [8, 12, 6, 10, 10, 10]),
        (1, [], [0]),
        (2, [[1, 0]], [1, 1]),
    ],
)
def test_lc_834_sum_of_distances(n, edges, expected):
    sol = _load_solution("0834_sum_of_distances_in_tree.py")
    assert sol.sumOfDistancesInTree(n, edges) == expected


@pytest.mark.parametrize(
    "n,edges,expected",
    [
        (4, [[1, 0], [1, 2], [1, 3]], [1]),
        (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]),
        (1, [], [0]),
        (2, [[0, 1]], [0, 1]),
    ],
)
def test_lc_310_minimum_height_trees(n, edges, expected):
    sol = _load_solution("0310_minimum_height_trees.py")
    assert sorted(sol.findMinHeightTrees(n, edges)) == expected
