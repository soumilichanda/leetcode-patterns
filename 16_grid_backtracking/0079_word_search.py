"""
LeetCode 79: Word Search
Difficulty: Medium
Pattern: Backtracking (2D Grid DFS Boundary Traversal)

Invariant:
    Explore 4-directional matrix moves.
    Temporarily mask visited cells with '#' to maintain O(1) auxiliary space.
    Backtrack original character on return.
    Early-exit frequency prune if board lacks characters.

Time Complexity: O(M * N * 4^L) where L is length of word
Space Complexity: O(L) recursion stack depth
"""

from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Frequency pruning optimization
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        if any(word_counts[c] > board_counts[c] for c in word_counts):
            return False

        # If reverse has less branching factor, reverse word
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False

            temp = board[r][c]
            board[r][c] = "#"  # Mask cell in-place

            found = (
                dfs(r + 1, c, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r, c - 1, idx + 1)
            )

            board[r][c] = temp  # Backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    sol = Solution()
    print("LC 79 Word Search ('ABCCED'):", sol.exist(board, "ABCCED"))
    print("LC 79 Word Search ('ABCB'):", sol.exist(board, "ABCB"))
