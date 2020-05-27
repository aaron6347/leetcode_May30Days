"""day25_uncrossed_lines.py
    Created by Aaron at 25-May-20"""
from typing import List
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # app1
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(n)[::-1]:
                if A[i] == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[n]

        # app2
        # import collections
        # dp, m, n = collections.defaultdict(int), len(A), len(B)
        # for i in range(m):
        #     for j in range(n):
        #         dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        # return dp[m - 1, n - 1]

        # app3
        # dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (A[i] == B[j]))
        # return dp[-1][-1]

run=Solution()
a,b=[1,4,2],[1,2,4]
print(run.maxUncrossedLines(a,b))
# app1 dp with 1 dimension
# app2 dp with 2 dimension from bottom right to top left
# app3 dp with 2 dimentsion top left to bottom right