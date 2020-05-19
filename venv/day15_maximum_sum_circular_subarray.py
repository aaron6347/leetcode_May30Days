"""day15_maximum_sum_circular_subarray.py
    Created by Aaron at 16-May-20"""
from typing import List
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # app1
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum

        # app2
        # if max(A) <= 0: return max(A)
        # endmax = [i for i in A]
        # endmin = [i for i in A]
        # for i in xrange(1, len(A)):
        #     if endmax[i - 1] > 0: endmax[i] += endmax[i - 1]
        #     if endmin[i - 1] < 0: endmin[i] += endmin[i - 1]
        # return max(max(endmax), sum(A) - min(endmin))

run=Solution()
a=[3,-1,2,-1]
print(run.maxSubarraySumCircular(a))
# app1 find max and min without circular with variables only
# app2 find max and min without circular with list