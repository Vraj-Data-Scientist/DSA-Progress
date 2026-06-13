from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, postorder: List[int], inorder: List[int]) -> TreeNode:
        map_ino = {val : idx for idx, val in enumerate(inorder)}
        def build(p_s, p_e, i_s, i_e):
            if p_s > p_e or i_s > i_e:
                return None
            root_val = postorder[p_e]
            root = TreeNode(root_val)
            ino_root_idx = map_ino[root_val]
            ino_left = ino_root_idx - i_s
            root.left = build(p_s, p_s+ino_left-1, i_s, ino_root_idx-1)
            root.right = build(p_s+ino_left, p_e-1, ino_root_idx+1, i_e)
            return root
        return build(0, len(postorder)-1, 0, len(inorder)-1)

    def inorderTraversal(self, root) -> List[int]:
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result

root = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
print(Solution().inorderTraversal(root))
