"""
LeetCode 133: Clone Graph
Difficulty: Medium
Pattern: Cluster 22 — Graphs (Deep State Duplication via Hash Map DFS)

Time Complexity: O(V + E)
Space Complexity: O(V) auxiliary visited mapping and recursion stack
"""

from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        cloned_map: Dict[Node, Node] = {}

        def dfs(curr: Node) -> Node:
            if curr in cloned_map:
                return cloned_map[curr]

            clone = Node(curr.val)
            cloned_map[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


if __name__ == "__main__":
    sol = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)

    cloned = sol.cloneGraph(node1)
    assert cloned is not None
    assert cloned.val == 1
    assert cloned.neighbors[0].val == 2
    assert cloned is not node1
    print("LC 133 (Clone Graph): Passed deep node virtualization assertion")
