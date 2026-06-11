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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dict1 = {}
        q = deque()
        q.append((root, 0, 0))
        while q:
            temp, x, y = q.popleft()
            dict1[y] = temp.val
            if temp.left:
                q.append((temp.left, x-1, y+1))
            if temp.right:
                q.append((temp.right, x+1, y+1))
        ans = []
        for y in sorted(dict1.keys()):
            ans.append(dict1[y])
        return ans

    def leftSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dict1 = {}
        q = deque()
        q.append((root, 0, 0))
        while q:
            temp, x, y = q.popleft()
            if y not in dict1:
                dict1[y] = temp.val
            if temp.left:
                q.append((temp.left, x-1, y+1))
            if temp.right:
                q.append((temp.right, x+1, y+1))
        ans = []
        for y in sorted(dict1.keys()):
            ans.append(dict1[y])
        return ans

    def rightSideView_DFS_inorder(self, root: TreeNode) -> List[int]:
        dict1 = {}
        def dfs(node, x, y):
            if not node:
                return
            dfs(node.left, x-1, y+1)
            dict1[y] = node.val
            dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        ans = []
        for y in sorted(dict1.keys()):
            ans.append(dict1[y])
        return ans

    def rightSideView_DFS_reverse_preorder(self, root: TreeNode, level) -> List[int]:
        ds = []
        def dfs(node, y):
            if not node:
                return
            if (y == len(ds)):
                ds.append(node.val)
            dfs(node.right, y+1)
            dfs(node.left, y+1)
        dfs(root, 0)
        return ds


print(Solution().rightSideView(node1))
print(Solution().leftSideView(node1))
print(Solution().rightSideView_DFS_inorder(node1))
print(Solution().rightSideView_DFS_reverse_preorder(node1, 0))