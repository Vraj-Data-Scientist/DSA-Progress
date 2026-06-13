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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        curr = root
        while curr is not None:
            if curr.left is None:
                inorder.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        return inorder

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder = []
        curr = root
        while curr is not None:
            if curr.left is None:
                preorder.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
                if node.right is None:
                    node.right = curr
                    preorder.append(curr.val)
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right
        return preorder

print(Solution().inorderTraversal(node1))
print(Solution().preorderTraversal(node1))
