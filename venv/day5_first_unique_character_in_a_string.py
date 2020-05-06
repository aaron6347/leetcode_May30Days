"""day5_first_unique_character_in_a_string.py
    Created by Aaron at 05-May-20"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # app1
        # from collections import OrderedDict
        # dic=OrderedDict()
        # dic2={}
        # for i, x in enumerate(s):
        #     if x not in dic and x not in dic2:
        #         dic[x]=i
        #     elif x in dic:
        #         del dic[x]
        #         dic2[x]=i
        # if dic:
        #     return list(dic.values())[0]
        # return -1

        # app2
        # from collections import Counter
        # ans=Counter(s)
        # for i, char in enumerate(s):
        #     if ans[char]==1:
        #         return i
        # return -1

run=Solution()
a='loveleetcode'
print(run.firstUniqChar(a))
# app1 use ordereddict and dic to store unique and non unique along traversal, time O(n) space O(n)
