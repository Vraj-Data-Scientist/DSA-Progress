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
    def countNodes_brute(self, root: TreeNode) -> int:
        counter = 0
        def dfs(root):
            nonlocal counter
            if not root:
                return None
            counter += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return counter

    def findHeightLeft(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def findHeightRight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh = self.findHeightLeft(root)
        rh = self.findHeightRight(root)
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

print(Solution().countNodes(node1))
print(Solution().countNodes_brute(node1))