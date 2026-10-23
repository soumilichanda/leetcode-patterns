"""
LeetCode 212: Word Search II
Difficulty: Hard
Pattern: Trie Prefix Pruning + 2D Matrix DFS Backtracking

Time Complexity: O(M * N * 4 * 3^(L-1)) where L is maximum word length
Space Complexity: O(K * L) where K is number of words, L is max word length for Trie
"""

from typing import List, Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: Optional[str] = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build Trie from word list
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        matched_words: List[str] = []

        # 2. In-place DFS backtracking with Trie node tracking
        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            curr_node = parent_node.children.get(char)
            if not curr_node:
                return

            # Check for word match
            if curr_node.word:
                matched_words.append(curr_node.word)
                curr_node.word = None  # Deduplicate matches

            # Mark visited
            board[r][c] = "#"

            # Explore 4-directional neighbors
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    if board[nr][nc] in curr_node.children:
                        dfs(nr, nc, curr_node)

            # Restore board (backtrack)
            board[r][c] = char

            # Optimization: prune leaf nodes to accelerate subsequent traversals
            if not curr_node.children:
                parent_node.children.pop(char, None)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return matched_words


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    res = sol.findWords(board, words)
    assert sorted(res) == sorted(["eat", "oath"]), f"Unexpected: {res}"
    print("LC 212 Word Search II invariant validated successfully!")
