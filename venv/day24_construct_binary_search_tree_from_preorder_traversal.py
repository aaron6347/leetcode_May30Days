"""day24_construct_binary_search_tree_from_preorder_traversal.py
    Created by Aaron at 24-May-20"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printLevelOrder(self, root):
        h = self.height(root)
        ar=[]
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
            ar.append("%d" % (root.val))
        elif level > 1:
            self.printGivenLevel(root.left, level - 1, ar)
            self.printGivenLevel(root.right, level - 1, ar)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = cur = TreeNode(preorder[0])
        x = 1
        while x < len(preorder):
            if cur.left is None and preorder[x] < cur.val:
                cur.left = TreeNode(preorder[x])
            elif cur.right is None and preorder[x] > cur.val:
                cur.right = TreeNode(preorder[x])
            elif preorder[x] < cur.val:
                cur = cur.left
                continue
            elif preorder[x] > cur.val:
                cur = cur.right
                continue
            cur = root
            x += 1
        return root

run=Solution()
a=[8,5,1,7,10,12]
root=run.bstFromPreorder(a)
root.printLevelOrder(root)
# understand binary search tree conditions