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
    def inorderTraversal(self, root) -> List[int]:
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result

    def change_tree(self, root):
        if not root:
            return None
        child = 0
        if root.left:
            child += root.left.val
        if root.right:
            child += root.right.val
        if child > root.val:
            root.val = child
        else:
            if root.left:
                root.left.val = root.val
            if root.right:
                root.right.val = root.val
        self.change_tree(root.left)
        self.change_tree(root.right)
        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val
        if root.left or root.right:
            root.val = total

print(Solution().inorderTraversal(node1))
Solution().change_tree(node1)
print(Solution().inorderTraversal(node1))
