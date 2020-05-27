"""day20_kth_smallest_element_in_a_bst.py
    Created by Aaron at 21-May-20"""
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # app1
        # stack = []
        # while True:
        #     while root.val is not None:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if not k:
        #         return root.val
        #     root = root.right

        # app2
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r.left is not None else []
        return inorder(root)[k - 1]

run=Solution()
a,b=[3,1,4,None,2],1
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
print(run.kthSmallest(node, b))
# app1 iteration with stack in-order traversal
# app2 recursive in-order traversal