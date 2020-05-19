"""day13_remove_k_digits.py
    Created by Aaron at 14-May-20"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # app1
        # res = []
        # for x in num:
        #     while k and res and res[-1] > x:
        #         res.pop()
        #         k -= 1
        #     res.append(x)
        # return ''.join(res[:-k or None]).lstrip('0') or '0' #if k has become 0 will return nothing, use 'or None' will make it choose None and return all elements

        # app2
        sub = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]|7[0-6]|8[0-7]|9[0-8]|.$').sub
        for _ in range(k):
            num = sub(lambda m: m.group()[1:], num, 1)
        return num.lstrip('0') or '0'

run=Solution()
a,b="1432219",3
print(run.removeKdigits(a,b))
# app1 monotonic queue, use stack to store and compare current with previous element, if bigger then pop else skip
# app2 k times remove the leftmost digit followed by a smaller digit (or remove the last digit)