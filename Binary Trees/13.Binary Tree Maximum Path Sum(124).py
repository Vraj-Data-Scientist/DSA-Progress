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
    def maxPathSum_helper(self, root: TreeNode, maxi) -> int:
        if not root:
            return 0
        ls = max(0, self.maxPathSum_helper(root.left, maxi))
        rs = max(0, self.maxPathSum_helper(root.right, maxi))
        self.maxi = max(self.maxi, (root.val + ls + rs))
        return root.val + max(ls , rs)

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi = float('-inf')
        self.maxPathSum_helper(root, self.maxi)
        return self.maxi

print(Solution().maxPathSum(node1))