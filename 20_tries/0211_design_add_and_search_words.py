"""
LeetCode 211: Design Add and Search Words Data Structure
Difficulty: Medium
Pattern: Cluster 20 — Trie with Recursive Backtracking DFS Wildcards

Time Complexity:
    - addWord(word): O(L)
    - search(word):  O(L) standard lookup, O(26^L) worst-case wildcard '.'
Space Complexity: O(N * L) node allocations
"""

class WordDictionaryNode:
    def __init__(self):
        self.children: dict[str, "WordDictionaryNode"] = {}
        self.is_end: bool = False


class WordDictionary:
    def __init__(self):
        self.root = WordDictionaryNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionaryNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx: int, node: WordDictionaryNode) -> bool:
            curr = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_end

        return dfs(0, self.root)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    assert wd.search("b...") is False
    print("LC 211 WordDictionary verified successfully!")
