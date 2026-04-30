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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        st = []
        res = []
        node = root
        last_visited = None   # Helps track the right child we've already processed
        while node or st:
            if node:
                st.append(node)
                node = node.left
            else:
                peek_node = st[-1]
                if peek_node.right and last_visited != peek_node.right:
                    node = peek_node.right
                else:
                    res.append(peek_node.val)
                    last_visited = st.pop()
        return res

print(Solution().postorderTraversal(node1))


