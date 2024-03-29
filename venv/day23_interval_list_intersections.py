"""day23_interval_list_intersections.py
    Created by Aaron at 23-May-20"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans

run=Solution()
a,b=[[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]
print(run.intervalIntersection(a,b))
# use 2 pointer, start with A[0] to be with B[0] and alternatively, B[0] with A[0] and so on