"""
LeetCode 167: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Pattern: Two Pointers (Inward Monotonic Search)

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
      current_sum = numbers[left] + numbers[right]
      if current_sum == target:
        return [left + 1, right + 1]
      elif current_sum < target:
        left += 1
      else:
        right -= 1

    return []