"""day12_single_element_in_a_sorted_array.py
    Created by Aaron at 13-May-20"""
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

run=Solution()
a=[3,3,7,7,10,11,11]
print(run.singleNonDuplicate(a))
# binary search use XOR to find odd or even, knowing odd even can help in checking which one (left or right)