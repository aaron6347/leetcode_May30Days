"""day3_ransom_note.py
    Created by Aaron at 03-May-20"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # app1
        # dic={}
        # for x in range(len(ransomNote)):
        #     if ransomNote[x] not in dic:
        #         dic[ransomNote[x]]=1
        #     else:
        #         dic[ransomNote[x]]=dic[ransomNote[x]]+1
        #
        # for x in range(len(magazine)):
        #     if magazine[x] not in dic:
        #         pass
        #     elif magazine[x] in dic:
        #         dic[magazine[x]]-=1
        #         if dic[magazine[x]]==0:
        #             del dic[magazine[x]]
        # return len(dic)==0

        # app2
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

        # app3
        # for i in set(ransomNote):
        #     if ransomNote.count(i) > magazine.count(i):
        #         return False
        # return True

run=Solution()
a,b="aba","aaab"
print(run.canConstruct(a,b))
# app1 using dictionary store ransomNote and traverse magazine to calculate difference, time O(n+m) space O(n)/O(m)
# app2 using collections counter, time O(n+m) space O(n)/O(m)
# app3 using count, time O(nm) space O(1)