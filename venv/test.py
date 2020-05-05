"""test.py
    Created by Aaron at 04-May-20"""
a=5
# 110
# 111
# 001+1
print(~a)
print((1<<a.bit_length())-1)
print(~a & (1<<a.bit_length())-1)