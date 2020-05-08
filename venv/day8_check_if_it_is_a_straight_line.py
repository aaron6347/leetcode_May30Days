"""day8_check_if_it_is_a_straight_line.py
    Created by Aaron at 08-May-20"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # app1
        if len(coordinates) == 2:
            return True
        A, B = coordinates[0][1] - coordinates[1][1], coordinates[1][0] - coordinates[0][0]
        C = -A*coordinates[0][0] - B*coordinates[0][1]
        for point in coordinates:
            if A*point[0] + B*point[1] + C != 0:
                return False
        return True

        # app2
        # x1,y1,x2,y2 = coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1]
        # for i in range(2, len(coordinates)):
        #     x,y = coordinates[i][0], coordinates[i][1]
        #     if ((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
        #         return False
        # return True

run=Solution()
a=[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(run.checkStraightLine(a))
# app1 algebra Ax+By+C=0 concept
# app2 checking the slope by (y-y1)/(y2-y1)=(x-x1)/(x2-x1) that requires 3 coordinates

