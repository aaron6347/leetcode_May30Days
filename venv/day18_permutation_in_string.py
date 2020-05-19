"""day18_permutation_in_string.py
    Created by Aaron at 19-May-20"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # app1
        # A = [ord(x) - ord('a') for x in s1]
        # B = [ord(x) - ord('a') for x in s2]
        # target = [0] * 26
        # for x in A:
        #     target[x] += 1
        # window = [0] * 26
        # for i, x in enumerate(B):
        #     window[x] += 1
        #     if i >= len(A):
        #         window[B[i - len(A)]] -= 1
        #     if window == target:
        #         return True
        # return False

        # app2
        import collections
        ctr1 = collections.defaultdict(int)
        ctr2 = collections.defaultdict(int)
        for x in s1:
            ctr1[x] += 1
        for x in s2[:len(s1)]:
            ctr2[x] += 1
        i = 0
        j = len(s1)
        while j < len(s2):
            if ctr2 == ctr1:
                return True
            ctr2[s2[i]] -= 1
            if ctr2[s2[i]] < 1:
                ctr2.pop(s2[i])
            ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
            i += 1
            j += 1
        return ctr2 == ctr1

        # app3
        # import collections
        # ctr1 = collections.Counter(s1)
        # i = 0
        # while i < len(s2) - len(s1) + 1:
        #     if s2[i] in ctr1:
        #         ctr2 = collections.Counter(s2[i: i + len(s1)])
        #         if ctr1 == ctr2:
        #             return True
        #     i += 1
        # return False

        # app4
        # import collections
        # ctr1 = collections.Counter(s1)
        # ctr2 = collections.Counter(s2[:len(s1)])
        # i = 0
        # j = len(s1)
        # while j < len(s2):
        #     if ctr2 == ctr1:
        #         return True
        #     ctr2[s2[i]] -= 1
        #     if ctr2[s2[i]] < 1:
        #         ctr2.pop(s2[i]);
        #     ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
        #     i += 1
        #     j += 1
        # return ctr2 == ctr1

run=Solution()
a,b="ab","eidbaooo"
print(run.checkInclusion(a,b))
# app1 use list and ord to symbol the index to store counter, 4 list
# app2 use collections defaultdict, 2 list only length of string
# app3 use collections Counter, slicing to check
# app4 use colections Counter, 2 pointers to check