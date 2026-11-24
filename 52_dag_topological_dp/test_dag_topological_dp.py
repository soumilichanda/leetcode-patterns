"""Parameterized test suite for Cluster 52: DAG Longest Paths & Topological Memoization DP."""

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
    "matrix,expected",
    [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
        ([[7, 7, 7], [7, 7, 7]], 1),
        ([[1, 2, 3, 4]], 4),
    ],
)
def test_longest_increasing_path(matrix, expected):
    sol = _load_solution("0329_longest_increasing_path_in_a_matrix.py")
    assert sol.longestIncreasingPath(matrix) == expected


@pytest.mark.parametrize(
    "colors,edges,expected",
    [
        ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3),
        ("a", [[0, 0]], -1),
        ("abc", [[0, 1], [1, 2], [2, 0]], -1),
        ("zzzz", [[0, 1], [1, 2], [2, 3]], 4),
        ("g", [], 1),
    ],
)
def test_largest_color_value_directed_graph(colors, edges, expected):
    sol = _load_solution("1857_largest_color_value_in_a_directed_graph.py")
    assert sol.largestPathValue(colors, edges) == expected
