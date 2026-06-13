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


class Codec:
    def serialize(self, root):
        if not root:
            return ""
        q = deque()
        q.append(root)
        result = ""
        while q:
            node = q.popleft()
            if not node:
                result += "#,"
            else:
                result += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
        return result

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque()
        q.append(root)
        i = 1
        while q and i < len(nodes) - 1:
            node = q.popleft()
            if nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != "#":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root

    def inorderTraversal(self, root) -> List[int]:
        result = []
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result


print(Codec().serialize(node1))
root = Codec().deserialize("1,2,3,4,5,6,7,#,#,#,#,#,#,#,#,")
print(Codec().inorderTraversal(root))