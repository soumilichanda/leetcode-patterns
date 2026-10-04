"""
LeetCode 704: Binary Search
Difficulty: Easy
Pattern: Binary Search (Classic Monotonic Invariant)

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
    ]

    print("=== LC 704: Binary Search Verification ===")
    for nums, target, expected in test_cases:
        actual = sol.search(nums, target)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] nums={nums}, target={target} -> Output: {actual} (Expected: {expected})")