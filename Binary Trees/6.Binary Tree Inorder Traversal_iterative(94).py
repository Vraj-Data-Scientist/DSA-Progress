from typing import List

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
        st = []
        res = []
        node = root
        while True:
            if node:
                st.append(node)
                node = node.left
            else:
                if not st:
                    break
                node = st.pop()
                res.append(node.val)
                node = node.right
        return res

print(Solution().inorderTraversal(node1))