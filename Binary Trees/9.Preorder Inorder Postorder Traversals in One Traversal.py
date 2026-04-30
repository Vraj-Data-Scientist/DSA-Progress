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
    def pre_in_post_one_traversal(self, root):
        pre = []
        ino = []
        post = []
        st = [(root, 1)]
        while st:
            node, state = st.pop()
            if (state == 1):
                pre.append(node.val)
                st.append((node, 2))
                if node.left:
                    st.append((node.left, 1))
            elif (state == 2):
                ino.append(node.val)
                st.append((node, 3))
                if node.right:
                    st.append((node.right, 1))
            else:
                post.append(node.val)
        return [pre, ino, post]

print(Solution().pre_in_post_one_traversal(node1))
