"""Parameterized test suite for Cluster 51: Bitmask Subsets & Assignment Optimization DP."""

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
    "nums,k,expected",
    [
        ([4, 3, 2, 3, 5, 2, 1], 4, True),
        ([1, 2, 3, 4], 3, False),
        ([2, 2, 2, 2, 3, 4, 5], 4, False),
        ([1, 1, 1, 1, 2, 2, 2, 2], 4, True),
        ([5], 1, True),
    ],
)
def test_partition_k_equal_sum_subsets(nums, k, expected):
    sol = _load_solution("0698_partition_to_k_equal_sum_subsets.py")
    assert sol.canPartitionKSubsets(list(nums), k) is expected


@pytest.mark.parametrize(
    "req_skills,people,expected_len",
    [
        (
            ["java", "nodejs", "reactjs"],
            [["java"], ["nodejs"], ["nodejs", "reactjs"]],
            2,
        ),
        (
            ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
            [
                ["algorithms", "math", "java"],
                ["algorithms", "math", "reactjs"],
                ["java", "csharp", "aws"],
                ["reactjs", "csharp"],
                ["csharp", "math"],
                ["aws", "java"],
            ],
            2,
        ),
    ],
)
def test_smallest_sufficient_team(req_skills, people, expected_len):
    sol = _load_solution("1125_smallest_sufficient_team.py")
    team = sol.smallestSufficientTeam(req_skills, people)
    assert len(team) == expected_len
    covered = set()
    for idx in team:
        covered.update(people[idx])
    assert set(req_skills).issubset(covered)
