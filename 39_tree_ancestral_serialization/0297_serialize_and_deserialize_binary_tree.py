"""
LeetCode 297: Serialize and Deserialize Binary Tree
Difficulty: Hard
Pattern: Tree DFS / Preorder Invariant Encoding

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional, Iterator


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens: list[str] = []

        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                tokens.append("#")
                return
            tokens.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens: Iterator[str] = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            token = next(tokens)
            if token == "#":
                return None
            node = TreeNode(int(token))
            node.left = build()
            node.right = build()
            return node

        return build()


if __name__ == "__main__":
    codec = Codec()
    # Tree: [1, 2, 3, None, None, 4, 5]
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = codec.serialize(root)
    assert serialized == "1,2,#,#,3,4,#,#,5,#,#", f"Unexpected serialization: {serialized}"

    deserialized = codec.deserialize(serialized)
    assert deserialized and deserialized.val == 1
    assert deserialized.left and deserialized.left.val == 2
    assert deserialized.right and deserialized.right.val == 3
    assert deserialized.right.left and deserialized.right.left.val == 4
    assert deserialized.right.right and deserialized.right.right.val == 5

    # Round-trip equality check
    round_trip = codec.serialize(deserialized)
    assert round_trip == serialized, "Round-trip serialization mismatch!"

    print("LC 297 (Serialize & Deserialize Binary Tree) verified successfully!")
