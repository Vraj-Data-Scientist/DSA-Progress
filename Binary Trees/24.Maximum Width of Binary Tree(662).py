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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None
        max_width = 0
        q = deque()
        q.append((root, 0))
        while q:
            size = len(q)
            mini_idx = q[0][1]
            first = 0
            last = 0
            for i in range(len(q)):
                node, idx = q.popleft()
                curr_idx = idx - mini_idx
                if i == 0:
                    first = curr_idx
                if i == size - 1:
                    last = curr_idx
                if node.left:
                    q.append((node.left, 2 * curr_idx + 1))
                if node.right:
                    q.append((node.right, 2 * curr_idx + 2))
            max_width = max(max_width, last - first + 1)
        return max_width

print(Solution().widthOfBinaryTree(node1))
