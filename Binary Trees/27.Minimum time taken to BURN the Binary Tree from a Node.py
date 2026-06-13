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
    def build_graph(self, root, dict1, target_val):
        q = deque()
        q.append(root)
        target_node = None
        while q:
            node = q.popleft()
            if node.val == target_val:
                target_node = node
            if node.left:
                dict1[node.left] = node
                q.append(node.left)
            if node.right:
                dict1[node.right] = node
                q.append(node.right)
        return target_node

    def find_min_time(self, root, target, dict1):
        q = deque()
        q.append(target)
        visited = set()
        visited.add(target)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                if node in dict1 and dict1[node] not in visited:
                    visited.add(dict1[node])
                    q.append(dict1[node])
            if q:
                level += 1
        return level

    def amountOfTime(self, root: TreeNode, start: int) -> int:
        if not root:
            return None
        dict1 = {}
        target_node = self.build_graph(root, dict1, start)
        return self.find_min_time(root, target_node, dict1)

print(Solution().amountOfTime(node1, 2))
