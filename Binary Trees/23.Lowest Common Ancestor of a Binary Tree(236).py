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
    def getpath(self, root, x, result):
        if not root:
            return False
        result.append(root)
        if root.val == x:
            return True
        if not self.getpath(root.left, x, result) and not self.getpath(root.right, x, result):
            result.pop()
            return False
        if self.getpath(root.left, x, result) or self.getpath(root.right, x, result):
            return True

    def getpath_better(self, root, x, result):
        if not root:
            return False
        result.append(root.val)
        if root.val == x:
            return True
        if self.getpath_better(root.left, x, result) or self.getpath_better(root.right, x, result):
            return True
        result.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        if not root:
            return None
        self.getpath_better(root, p.val, path1)
        self.getpath_better(root, q.val, path2)
        if not path1 or not path2:
            return None
        i, j = 0, 0
        intersection = -1
        while i < len(path1) and j < len(path2):
            if i == j and path1[i] == path2[j]:
                i += 1
                j += 1
            else:
                intersection = j - 1
                break
        if i == len(path1) or j == len(path2):
            intersection = min(i, j) - 1
        return path2[intersection]

    def lowestCommonAncestor_brute_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root.val
        if not self.lowestCommonAncestor_brute_2(root.left, p, q) and not self.lowestCommonAncestor_brute_2(root.right, p, q):
            return None
        elif self.lowestCommonAncestor_brute_2(root.left, p, q) and self.lowestCommonAncestor_brute_2(root.right, p, q):
            return root.val
        elif not self.lowestCommonAncestor_brute_2(root.left, p, q) and self.lowestCommonAncestor_brute_2(root.right, p, q):
            return self.lowestCommonAncestor_brute_2(root.right, p, q)
        elif self.lowestCommonAncestor_brute_2(root.left, p, q) and not self.lowestCommonAncestor_brute_2(root.right, p, q):
            return self.lowestCommonAncestor_brute_2(root.left, p, q)

    def lowestCommonAncestor_better(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor_better(root.left, p, q)
        right = self.lowestCommonAncestor_better(root.right, p, q)
        if not left and not right:
            return None
        elif left and right:
            return root
        elif not left and right:
            return right
        elif left and not right:
            return left

    def lowestCommonAncestor_optimal(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root.val
        left = self.lowestCommonAncestor_optimal(root.left, p, q)
        right = self.lowestCommonAncestor_optimal(root.right, p, q)
        if left and right:
            return root.val
        return left if left else right

print(Solution().lowestCommonAncestor(node1, node4, node5))
print(Solution().lowestCommonAncestor_brute_2(node1, node4, node5))
print(Solution().lowestCommonAncestor_optimal(node1, node4, node5))

