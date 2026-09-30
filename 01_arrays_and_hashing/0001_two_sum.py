"""
LeetCode 1: Two Sum
Difficulty: Easy
Pattern: Hash Map (Single-Pass Complement Lookup)

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:

  def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
      complement = target - num
      if complement in seen:
        return [seen[complement], i]
      seen[num] = i
    return []