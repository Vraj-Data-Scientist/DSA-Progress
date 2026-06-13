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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return None
        dict1 = {}
        self.map_parent(root, dict1)
        return self.level_k(root, target, k, dict1)

    def map_parent(self, root, dict1):
        q = deque()
        q.append(root)
        while q:
            root = q.popleft()
            if root.left:
                dict1[root.left] = root
                q.append(root.left)
            if root.right:
                dict1[root.right] = root
                q.append(root.right)

    def level_k(self, root, target, k, dict1):
        curr_level = 0
        visited = set()
        q = deque()
        q.append(target)
        visited.add(target)
        while q:
            if curr_level == k:
                break
            for _ in range(len(q)):
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
            curr_level += 1
        return [root.val for root in q]

print(Solution().distanceK(node1, node2, 1))

