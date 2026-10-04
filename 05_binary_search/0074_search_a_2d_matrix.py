"""
LeetCode 74: Search a 2D Matrix
Difficulty: Medium
Pattern: Binary Search (Virtualized 1D-to-2D Coordinate Projection)

Time Complexity: O(log(m * n))
Space Complexity: O(1)
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]

    test_cases = [
        (matrix1, 3, True),
        (matrix1, 13, False),
        ([[1]], 1, True),
        ([[1]], 0, False),
    ]

    print("=== LC 74: Search a 2D Matrix Verification ===")
    for mat, target, expected in test_cases:
        actual = sol.searchMatrix(mat, target)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] target={target:<3} -> Output: {actual:<5} (Expected: {expected})")