"""day19_stock_open_span.py
    Created by Aaron at 20-May-20"""
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

run=StockSpanner()
a=["StockSpanner","next","next","next","next","next","next","next","next","next"]
b=[[],[100],[80],[60],[70],[60],[75],[85], [100],[101]]
res=[]
for x in range(1,len(a)):
    res.append(eval("run.{0}({1})".format(a[x], b[x][0])))
print(res)
# use stack to operate