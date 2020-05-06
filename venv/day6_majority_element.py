"""day6_majority_element.py
    Created by Aaron at 06-May-20"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # app1
        # if len(nums)<3:
        #     return nums[0]
        # dic={}
        # n=len(nums)
        # for x in range(n):
        #     if nums[x] not in dic:
        #         dic[nums[x]]=1
        #     else:
        #         dic[nums[x]]+=1
        #         if dic[nums[x]]>n//2:
        #             return nums[x]

        # app2
        # if len(nums) < 3:
        #     return nums[0]
        # dic = {}
        # n = len(nums)
        # l, r = 0, n - 1
        # while l <= r:
        #     if nums[l] not in dic:
        #         dic[nums[l]] = 1
        #     else:
        #         dic[nums[l]] += 1
        #         if dic[nums[l]] > n // 2:
        #             return nums[l]
        #     if nums[r] not in dic:
        #         dic[nums[r]] = 1
        #     else:
        #         dic[nums[r]] += 1
        #         if dic[nums[r]] > n // 2:
        #             return nums[r]
        #     l += 1
        #     r -= 1

        # app3
        # import collections
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)

        # app4
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

run=Solution()
a=[3,2,3]
print(run.majorityElement(a))
# app1 brute force counting all in dictionary, time O(n)
# app2 similar to app1 but using two pointer left and right, time O(n/2) space O(n)
# app3 similar to app1 but using collectionscounter, time O(n) space O(n)
# app4 boyer-moore voting algorithm, choose a candidate, if next is not candidate, minus count, if same, pls count, time O(n) space O(1)