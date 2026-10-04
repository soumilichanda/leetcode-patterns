"""
LeetCode 875: Koko Eating Bananas
URL: https://leetcode.com/problems/koko-eating-bananas/
Difficulty: Medium
Pattern: Binary Search on the Answer Space (Monotonic Feasibility)

Time Complexity: O(n * log(max(piles)))
Space Complexity: O(1)
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid_k = left + (right - left) // 2
            
            # Integer ceil arithmetic: (p + mid_k - 1) // mid_k
            total_hours = sum((p + mid_k - 1) // mid_k for p in piles)

            if total_hours <= h:
                ans = mid_k
                right = mid_k - 1
            else:
                left = mid_k + 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ]

    print("=== LC 875: Koko Eating Bananas Verification ===")
    for piles, h, expected in test_cases:
        actual = sol.minEatingSpeed(piles, h)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] piles={piles}, h={h} -> Min Speed: {actual} (Expected: {expected})")
        