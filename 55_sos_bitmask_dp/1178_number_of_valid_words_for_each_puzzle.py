"""
LeetCode 1178: Number of Valid Words for Each Puzzle
Difficulty: Hard
Pattern: Cluster 55 — Bitmask Frequency Compression & Submask Enumeration

Invariant:
    1. Encode each word into a 26-bit character-set bitmask. Words with popcount > 7
       cannot be covered by any 7-letter puzzle and are pruned immediately.
    2. For each 7-character puzzle, every valid word mask must:
       (a) Contain `first_bit` (the bit corresponding to puzzle[0]).
       (b) Be a submask of the full 7-letter puzzle bitmask.
    3. Enumerate all 2^6 = 64 submasks of `tail_mask` (the other 6 puzzle characters)
       using `sub = (sub - 1) & tail_mask` and sum `freq[sub | first_bit]`.

Time Complexity: O(W * L_w + P * 2^6)
Space Complexity: O(W)
"""

from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        mask_freq: Counter[int] = Counter()

        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))
            if mask.bit_count() <= 7:
                mask_freq[mask] += 1

        results: List[int] = []
        for puzzle in puzzles:
            first_bit = 1 << (ord(puzzle[0]) - ord("a"))
            tail_mask = 0
            for ch in puzzle[1:]:
                tail_mask |= 1 << (ord(ch) - ord("a"))

            valid_count = 0
            sub = tail_mask
            while True:
                valid_count += mask_freq[sub | first_bit]
                if sub == 0:
                    break
                sub = (sub - 1) & tail_mask

            results.append(valid_count)

        return results


if __name__ == "__main__":
    sol = Solution()
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    assert sol.findNumOfValidWords(words, puzzles) == [1, 1, 3, 2, 4, 0]
    print("LC 1178 verified successfully!")
