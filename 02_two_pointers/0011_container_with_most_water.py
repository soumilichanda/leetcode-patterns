"""
LeetCode 11: Container With Most Water
Difficulty: Medium
Pattern: Two Pointers (Greedy Inward Shrink)

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

  def maxArea(self, height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
      current_width = right - left
      current_height = min(height[left], height[right])
      current_area = current_width * current_height

      if current_area > max_water:
        max_water = current_area

      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return max_water