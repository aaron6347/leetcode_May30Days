"""day7_cousins_in_binary_tree.py
    Created by Aaron at 07-May-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # insert by 1,2,4,8,16,32,64
    def insert(self, root, n, middle, times):
        if times > 0:
            if n <= middle:
                self.left.insert(root, n, middle - 2, times - 1)
            else:
                self.right.insert(root, n, middle + 2, times - 1)
        else:
            if n % 2 == 1:
                self.left = TreeNode(root)
            elif n % 2 == 0:
                self.right = TreeNode(root)

    # print
    def printLevelOrder(self, root):
        h = self.height(root)
        ar = []
        for i in range(1, h + 1):
            self.printGivenLevel(root, i, ar)
        print(ar)

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printGivenLevel(self, root, level, ar):
        if root is None:
            ar.append(None)
            return
        if level == 1:
            ar.append((root.val))
        elif level > 1:
            self.printGivenLevel(root.left, level - 1, ar)
            self.printGivenLevel(root.right, level - 1, ar)

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # app1
        # def dfs(root, target, depth, par):
        #     if root :
        #         if root.val==target:
        #             return (depth, par)
        #         return dfs(root.left, target, depth+1, root.val) or dfs(root.right, target, depth+1, root.val)
        # return dfs(root, x, 0, -1)[0]==dfs(root, y, 0, -1)[0] and dfs(root, x, 0, -1)[1]!=dfs(root, y, 0, -1)[1]

        # app2
        g = {}
        def f(root, i=0, parentVal=None):
            if root == None:
                return
            g[root.val] = (i, parentVal)
            f(root.left, i + 1, parentVal=root.val)
            f(root.right, i + 1, parentVal=root.val)
        f(root)
        return g[x][0] == g[y][0] and g[x][1] != g[y][1]

        # app3
        # import collections
        # nodes = collections.defaultdict(list)
        # queue = [(root, 0, 0)]
        # while queue:
        #     node, level, parent = queue.pop(0)
        #     nodes[node.val] = [level, parent]
        #     if node.left:
        #         queue.append((node.left, level + 1, node.val))
        #     if node.right:
        #         queue.append((node.right, level + 1, node.val))
        #
        # if nodes[x][0] == nodes[y][0] and nodes[x][1] != nodes[y][1]:
        #     return True
        # return False

run=Solution()
a,b,c=[1,2,3,None,4,None,5],5,4
copy=a
i=0
while i<len(a):
    if all ( y is None for y in a[i:-1]):
        break
    if a[i]==None:
        copy.insert(i * 2 + 1, None)
        copy.insert(i * 2 + 2, None)
    i+=1
    a=copy
for x in range(len(a)-1, -1,-1):    # cutting the extra None at the end list
    if a[x]!=None:
        i=x
        break
a=a[:i+1]
node = TreeNode(a[0])
bi=[2,4,8,16,32,64] # symmetry binary tree
for x in range(1, len(a)):
    sum=0
    for y in range(len(bi)):
        sum+=bi[y]
        if x<=sum:
            node.insert(a[x], x, sum-bi[y]+(bi[y]/2), y)
            break
# node.printLevelOrder(node)
print(run.isCousins(node, b, c))
# app1 dfs with x and y to traverse and find each own target, time O(2n) space O(1)
# app2 dfs with dictionary to store all parents and value, time O(n) space O(n)
# app3 recursive queue method with default dictionary from collections timeO(n) space O(n)
