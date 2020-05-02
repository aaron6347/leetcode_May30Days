"""day2_jewels_and_stones.py
    Created by Aaron at 02-May-20"""
class Solution:
    # app1
    # def numJewelsInStones(self, J: str, S: str) -> int:
    #     dic={x for x in J}
    #     ans=0
    #     for x in S:
    #         if x in dic:
    #             ans+=1
    #     return ans

    # app2
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic = {x for x in J}
        return sum(x in dic for x in S)

    # app3
    # def numJewelsInStones(self, J: str, S: str) -> int:
    #     return sum(map(J.count, S))

run=Solution()
a,b="aA","aAAbbbb"
print(run.numJewelsInStones(a,b))
# app1 J in dictionary and traverse S and check the dictonary, time O(m+n) space O(m)/O(n)
# app2 similar to app1 but using sum, time O(m+n) space O(m)/O(n)
# app3 check frequently, time O(mn) space O(1)