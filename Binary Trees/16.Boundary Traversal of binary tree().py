from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

class Solution:
    def is_leaf(self, root):
        return (root.left is None and root.right is None)

    def collect_left_boundary(self, root, res):
        node = root.left
        while node:
            if not self.is_leaf(node):
                res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

    def collect_right_boundary(self, root, res):
        temp = []
        node = root.right
        while node:
            if not self.is_leaf(node):
                temp.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        for i in range(len(temp)-1, -1, -1):
            res.append(temp[i])

    def collect_leaves(self, root, res):
        if self.is_leaf(root):
            res.append(root.val)
            return
        if root.left:
            self.collect_leaves(root.left, res)
        if root.right:
            self.collect_leaves(root.right, res)

    def boundaryTraversal(self, root):
        res = []
        if not root:
            return res
        if not self.is_leaf(root):
            res.append(root.val)
        self.collect_left_boundary(root, res)
        self.collect_leaves(root, res)
        self.collect_right_boundary(root, res)
        return res

print(Solution().boundaryTraversal(node1))



