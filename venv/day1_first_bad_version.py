"""day1_first_bad_version.py
    Created by Aaron at 01-May-20"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=1,n
        while l<r:
            middle=l+(r-l)//2
            if isBadVersion(middle):
                r=middle
            else:
                l=middle+1
        return l

def isBadVersion(number):
    return default[number]

run=Solution()
a,b=5,2
default={x:False if x< b else True for x in range(1,a+1)}
print(run.firstBadVersion(a))
# binary search from middle, if true go to right side by changing r, otherwise go left side by changing l