"""day26_contiguous_array.py
    Created by Aaron at 26-May-20"""
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx=0
        count=0
        dict={0: -1}
        for x,val in enumerate(nums):
            count-=1 if val==0 else -1
            if count in dict:
                mx=max(mx, x-dict[count])
            else:
                dict[count]=x
        return mx

run=Solution()
# a=[1,0]
a=[0,0,1,0,0,0,1,1]
print(run.findMaxLength(a))
# idea can be retrieve from day5 best time to buy and sell stock where let 0 and 1 as the movement of graph going down and up
# each time a point reencounter means there is a subarray