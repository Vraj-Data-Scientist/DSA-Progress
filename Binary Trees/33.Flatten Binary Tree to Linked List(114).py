from typing import List
from collections import deque

from Scripts.activate_this import prev_length


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

    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                node = curr.left
                while node.right:
                    node = node.right
                node.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

print(Solution().inorderTraversal(node1))
Solution().flatten(node1)
print(Solution().inorderTraversal(node1))


