"""
LeetCode 982: Triples with Bitwise AND Equal To Zero
Difficulty: Hard
Pattern: Cluster 55 — Sum Over Subsets (SOS) & Bitwise Convolution DP

Invariant:
    1. Compute pairwise bitwise AND frequencies: pair_freq[a & b] += 1 for all a, b in nums.
    2. Apply Sum Over Subsets (SOS) DP across B bits so sos[mask] stores the total
       number of pairs (a, b) such that (a & b) is a submask of `mask`.
    3. For each element z in nums, `(a & b) & z == 0` holds iff `(a & b)` is a submask
       of the bitwise complement `full_mask ^ z`. Accumulate sos[full_mask ^ z].

Time Complexity: O(n^2 + B * 2^B) where B = bit_length(max(nums)) <= 16
Space Complexity: O(2^B)
"""

from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_val = max(nums)
        bits = max(1, max_val.bit_length())
        size = 1 << bits
        full_mask = size - 1

        sos = [0] * size
        for a in nums:
            for b in nums:
                sos[a & b] += 1

        # Sum Over Subsets (SOS) DP: accumulate submask frequencies across each bit dimension
        for bit in range(bits):
            bit_mask = 1 << bit
            for mask in range(size):
                if mask & bit_mask:
                    sos[mask] += sos[mask ^ bit_mask]

        total_triplets = 0
        for z in nums:
            complement = full_mask ^ z
            total_triplets += sos[complement]

        return total_triplets


if __name__ == "__main__":
    sol = Solution()
    assert sol.countTriplets([2, 1, 3]) == 12
    assert sol.countTriplets([0, 0, 0]) == 27
    print("LC 982 verified successfully!")
