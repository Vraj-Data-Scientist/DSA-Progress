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
        result.append(root.val)
        if root.val == x:
            return True
        if self.getpath(root.left, x, result) or self.getpath(root.right, x, result):
            return True
        result.pop()
        return False

    def solve(self, root, x):
        result = []
        if not root:
            return result
        self.getpath(root, x, result)
        return result

    def path_bet_2_node(self, root, x, y):
        path1 = []
        path2 = []
        path = []
        if not root:
            return []
        self.getpath(root, x, path1)
        self.getpath(root, y, path2)
        i, j = 0, 0
        intersection = -1
        while (i != len(path1) or j != len(path2)):
            if (i == j and path1[i] == path2[j]):
                i += 1
                j += 1
            else:
                intersection = j - 1
                break
        for i in range(len(path1)-1, intersection-1, -1):
            path.append(path1[i])
        for j in range(intersection+1, len(path2)):
            path.append(path2[j])
        return path



print(Solution().solve(node1, 4))
print(Solution().path_bet_2_node(node1, 4, 5))
print(Solution().path_bet_2_node(node1, 4, 6))


