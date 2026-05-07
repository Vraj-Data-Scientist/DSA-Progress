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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return 1 + max(lh, rh)

    def isBalanced_1(self, root: TreeNode) -> bool:
        if not root:
            return True
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        if (abs(lh - rh) > 1):
            return False
        bool_left = self.isBalanced_1(root.left)
        bool_right = self.isBalanced_1(root.right)
        if (not bool_left or not bool_right):
            return False
        return True

    def isBalanced_2(self, root: TreeNode) -> bool:
        if not root:
            return True
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        if (abs(lh - rh) <= 1 and self.isBalanced_2(root.left) and self.isBalanced_2(root.right)):
            return True
        return False

    def isBalanced_helper(self, root: TreeNode):
        if not root:
            return 0
        lh = self.isBalanced_helper(root.left)
        rh = self.isBalanced_helper(root.right)
        if (lh == -1 or rh == -1):
            return -1
        if (abs(lh - rh) > 1):
            return -1
        return max(lh, rh) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalanced_helper(root) != -1

print(Solution().isBalanced_1(node1))
print(Solution().isBalanced_2(node1))
print(Solution().isBalanced(node1))