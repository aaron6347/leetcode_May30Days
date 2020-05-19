"""day11_flood_fill.py
    Created by Aaron at 11-May-20"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # app1
        # if image[sr][sc]==newColor:return image
        # def dfs(image, sr, sc, val, newval):
        #     if image[sr][sc] == val:
        #         image[sr][sc] = newval
        #         if sr - 1 >= 0: dfs(image, sr - 1, sc, val, newval)
        #         if sc - 1 >= 0: dfs(image, sr, sc - 1, val, newval)
        #         if sc + 1 < len(image[0]): dfs(image, sr, sc + 1, val, newval)
        #         if sr + 1 < len(image): dfs(image, sr + 1, sc, val, newval)
        #     return image
        # return dfs(image, sr, sc, image[sr][sc], newColor)

        # app2
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                        q.append((x, y))
        return image

        # app3
        # oriCol = image[sr][sc]
        # if oriCol == newColor: return image
        # row, col, surs = len(image), len(image[0]), [(sr, sc)]
        # while surs:
        #     for i, j in surs: image[i][j] = newColor
        #     surs = [(x, y) for i, j in surs for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]
        #              if 0<=x<row and 0<=y<col and image[x][y] == oriCol]
        # return image

run=Solution()
a,b,c,d=[[1,1,1],[1,1,0],[1,0,1]],1,1,2
print(run.floodFill(a,b,c,d))
# app1 dfs
# app2 bfs with deque
# app3 bfs