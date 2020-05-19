"""day10_find_the_town_judge.py
    Created by Aaron at 11-May-20"""
from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # app1
        # if N==1 and len(trust)==0: return 1
        # judge,town={},{}
        # for x in trust:
        #     town[x[0]]=x[0]
        #     if x[0] in judge:
        #         del judge[x[0]]
        #         continue
        #     if x[1] not in judge and x[1] not in town:
        #         judge[x[1]]=x[1]
        # if len(judge)==1:
        #     return list(judge)[0]
        # return -1

        # app2
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

run=Solution()
a,b=4,[[1,3],[1,4],[2,3],[2,4],[4,3]]
print(run.findJudge(a,b))
# app1 put town and judge, if it is judge before and now town, ignore its judge, judge length must be 1, time O(n) space O(n) n=length of trust
# app2 increment if judge, decrement if town, find whoever is N-1 which indicates everyone trust you, time O(n+t) space O(n) t=length of trust