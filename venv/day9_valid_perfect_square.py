"""day9_valid_perfect_square.py
    Created by Aaron at 10-May-20"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # app1
        # start = 1
        # while start ** 2 <= num:
        #     if start ** 2 == num:
        #         return True
        #     start += 1
        # return False

        # app2
        # if num < 0:
        #     return False
        # x, i = 0, 1
        # while x < num:
        #     x += i
        #     i += 2
        # return x == num

        # app3
        # l,r=0,num
        # while l<=r:
        #     mid=(l+r)//2
        #     if mid**2==num:
        #         return True
        #     elif mid**2>num:
        #         r=mid-1
        #     else:
        #         l=mid+1
        # return False

        # app4
        r = num
        while r * r > num:
            r = (r + num / r) // 2
        return r * r == num

        # app5
        # i = 1
        # while (num > 0):
        #     num -= i
        #     i += 2
        # return num == 0

        # app6
        # root = 0
        # bit = 1 << 15
        # while bit > 0:
        #     root |= bit
        #     if root > num // root:
        #         root ^= bit
        #     bit >>= 1
        # return root * root == num

run=Solution()
a=19
print(run.isPerfectSquare(a))
# app1 naive, increment 1 by 1 to find matching target or not, time O(sqrt(n))
# app2 1*1=1 (1+0), 2*2=4 (3+1), 3*3=9 (5+4), 4*4=16 (7+9), 5*5=25 (9+16), time O(sqrt(n))
# app3 binary search 2*2=4 (4>4/2) 3*3=9 (9>9/2), time O(log sqrt(n))
# app4 newton/ babylonian method in opposite decrement way
# app5 same concept as app2, but using 1 variable
# app6 bitwise trick