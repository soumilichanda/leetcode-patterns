"""
LeetCode 127: Word Ladder
Difficulty: Hard
Pattern: Cluster 23 — Graph BFS (Bidirectional Frontier BFS with Wildcard Bucketing)

Time Complexity: O(M^2 * N) where M is word length and N is word count
Space Complexity: O(M^2 * N) auxiliary wildcard map & set space
"""

from collections import defaultdict
from typing import List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set: Set[str] = set(wordList)
        if endWord not in word_set:
            return 0

        # Build intermediate wildcard patterns: d*g -> [dog, dig]
        word_len = len(beginWord)
        all_combos: defaultdict[str, List[str]] = defaultdict(list)
        for word in word_set:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]
                all_combos[pattern].append(word)

        # Bidirectional frontiers
        front_set: Set[str] = {beginWord}
        back_set: Set[str] = {endWord}
        visited: Set[str] = {beginWord, endWord}
        step_count = 1

        while front_set and back_set:
            # Always expand the smaller frontier to minimize branching factor
            if len(front_set) > len(back_set):
                front_set, back_set = back_set, front_set

            next_front: Set[str] = set()

            for word in front_set:
                for i in range(word_len):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in all_combos[pattern]:
                        if neighbor in back_set:
                            return step_count + 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_front.add(neighbor)

            front_set = next_front
            step_count += 1

        return 0


if __name__ == "__main__":
    sol = Solution()
    res1 = sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    assert res1 == 5, f"Expected 5, got {res1}"

    res2 = sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    assert res2 == 0, f"Expected 0, got {res2}"

    print("LC 127 (Word Ladder): All bidirectional BFS assertions passed successfully!")
