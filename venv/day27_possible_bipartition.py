"""day27_possible_bipartition.py
    Created by Aaron at 27-May-20"""
from typing import List
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # app1
        import collections
        graph, group = collections.defaultdict(set), {}
        for u, v in dislikes: graph[u].add(v), graph[v].add(u)
        def dfs(node, g):
            if node in group: return group[node] == g
            group[node] = g
            return all(dfs(nei, 1-g) for nei in graph[node])
        return all(dfs(node, 0) for node in range(1,N+1) if node not in group)

run=Solution()
a,b=4,[[1,2],[1,3],[2,4]]
print(run.possibleBipartition(a,b))
# app1 dfs recursive, separate the dislike into 2 graph making it bipartite graph and dfs both nodes where its children shud different from parent