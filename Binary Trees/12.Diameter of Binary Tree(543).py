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
    def __init__(self):
        self.maxi = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return 1 + max(lh, rh)

    def diameterOfBinaryTree_helper(self, root: TreeNode):
        if root is None:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        self.maxi = max(self.maxi, lh+rh)
        self.diameterOfBinaryTree_helper(root.left)
        self.diameterOfBinaryTree_helper(root.right)

    def diameterOfBinaryTree_brute(self, root: TreeNode) -> int:
        self.diameterOfBinaryTree_helper(root)
        return self.maxi

    def diameterOfBinaryTree_optimal_helper(self, root: TreeNode):
        if root is None:
            return 0
        lh = self.diameterOfBinaryTree_optimal_helper(root.left)
        rh = self.diameterOfBinaryTree_optimal_helper(root.right)
        self.maxi = max(self.maxi, lh+rh)
        return 1 + max(lh, rh)

    def diameterOfBinaryTree_optimal(self, root: TreeNode) -> int:
        self.diameterOfBinaryTree_optimal_helper(root)
        return self.maxi


# print(Solution().diameterOfBinaryTree_brute(node1))
print(Solution().diameterOfBinaryTree_optimal(node1))




