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
    def topView(self, root: TreeNode):
        if not root:
            return []
        dict1 = {}
        q = deque()
        q.append((root, 0))
        while q:
            temp, x = q.popleft()
            if x not in dict1:
                dict1[x] = temp.val
            if temp.left:
                q.append((temp.left, x-1))
            if temp.right:
                q.append((temp.right, x+1))
        ans = []
        for x in sorted(dict1.keys()):
            ans.append(dict1[x])
        return ans

    def topView_DFS_inorder(self, root: TreeNode):
        if not root:
            return []
        dict1 = {}    # column -> (value, depth)
        def dfs(node, x, y):
            if not node:
                return
            dfs(node.left, x-1, y+1)
            if x not in dict1 or y < dict1[x][1]:
                dict1[x] = (node.val, y)
            dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        ans = []
        for x in sorted(dict1.keys()):
            ans.append(dict1[x][0])
        return ans

print(Solution().topView(node1))
print(Solution().topView_DFS_inorder(node1))

