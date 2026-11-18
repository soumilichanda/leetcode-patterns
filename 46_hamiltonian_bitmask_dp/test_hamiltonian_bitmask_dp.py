import importlib.util
from pathlib import Path
import pytest

CLUSTER_DIR = Path(__file__).parent


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(filename[:-3], CLUSTER_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module.Solution()


@pytest.mark.parametrize(
    "graph,expected",
    [
        ([[]], 0),
        ([[1], [0]], 1),
        ([[1, 2, 3], [0], [0], [0]], 4),
        ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
    ],
)
def test_lc_0847_shortest_path_visiting_all_nodes(graph, expected):
    sol = _load("0847_shortest_path_visiting_all_nodes.py")
    assert sol.shortestPathLength(graph) == expected


@pytest.mark.parametrize(
    "words,expected_len",
    [
        (["alex", "loves", "leetcode"], 17),
        (["catg", "ctaagt", "gcta", "ttca", "atgcatc"], 16),
        (["abc", "bcd", "cde"], 5),
    ],
)
def test_lc_0943_shortest_superstring(words, expected_len):
    sol = _load("0943_find_the_shortest_superstring.py")
    ans = sol.shortestSuperstring(words)
    assert len(ans) == expected_len
    for w in words:
        assert w in ans
