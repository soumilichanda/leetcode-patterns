"""
LeetCode 155: Min Stack
Difficulty: Medium
Pattern: Stack (Synchronized Tuple State Tracking)

Time Complexity: O(1) for push, pop, top, getMin
Space Complexity: O(n)
"""


class MinStack:
    def __init__(self):
        # Stack stores tuples: (val, current_minimum_at_this_depth)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print("=== LC 155: Min Stack Verification ===")
    print(f"getMin(): {min_stack.getMin()} (Expected: -3)")
    min_stack.pop()
    print(f"top():    {min_stack.top()} (Expected: 0)")
    print(f"getMin(): {min_stack.getMin()} (Expected: -2)")