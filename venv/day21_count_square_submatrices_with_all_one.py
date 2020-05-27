"""day21_count_square_submatrices_with_all_one.py
    Created by Aaron at 22-May-20"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))

run=Solution()
a=[[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(run.countSquares(a))
# use dp find min of surrounding neighbour cell and +1 or just only 0 depends on its own value