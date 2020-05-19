"""day17_find_all_anagrams_in_a_string.py
    Created by Aaron at 19-May-20"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # app1
        # from collections import Counter
        # res = []
        # pCounter = Counter(p)
        # sCounter = Counter(s[:len(p)-1])
        # for i in range(len(p)-1,len(s)):
        #     sCounter[s[i]] += 1
        #     if sCounter == pCounter:
        #         res.append(i-len(p)+1)
        #     sCounter[s[i-len(p)+1]] -= 1
        #     if sCounter[s[i-len(p)+1]] == 0:
        #         del sCounter[s[i-len(p)+1]]
        # return res

        # app2
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0] * 123, [0] * 123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m - 1]:
            shash[ord(x)] += 1
        for i in range(m - 1, n):
            shash[ord(s[i])] += 1
            if i - m >= 0:
                shash[ord(s[i - m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

run=Solution()
a,b="cbaebabacd","abc"
print(run.findAnagrams(a,b))
# app1 use collections Counter
# app2 use list and ord