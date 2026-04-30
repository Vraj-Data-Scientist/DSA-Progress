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
    def preorderTraversal_brute(self, root) -> List[int]:
        res = []
        st = [root]
        while st:
            node = st.pop()
            res.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return res

    def preorderTraversal_optimized(self, root) -> List[int]:
        res = []
        st = []
        node = root
        while st or node:
            while node:
                res.append(node.val)
                if node.right:
                    st.append(node.right)
                node = node.left
            if st:
                node = st.pop()
        return res

print(Solution().preorderTraversal_brute(node1))
print(Solution().preorderTraversal_optimized(node1))




