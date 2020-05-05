"""day4_number_complement.py
    Created by Aaron at 04-May-20"""
class Solution:
    def findComplement(self, num: int) -> int:
        # app1
        # urbin=bin(num)[2:]
        # newbin='1'*len(urbin)
        # return int(newbin, 2)^num

        # app2
        # urbin = bin(num)
        # newbin='1'*(len(urbin)-2)
        # return int(newbin, 2)^num

        # app3
        # mask = 1 << (len(bin(num)) - 2)
        # return (mask - 1) ^ num

        # app4
        return ~num & (1 << num.bit_length()) - 1

run=Solution()
a=102
print(run.findComplement(a))
# app1 find its binary knowing its bit range boundary to do XOR
# app2 instead of slicing string, can just -2 length then XOR
# app3 find +1 left digit of bit range boundary by bit shifting then -1 it again to gain bit range boundary then XOR
# app4 negate the number, use AND with its bit range boundary eg ~5 to be 110 & 111 =   001+1 = 010 = 2