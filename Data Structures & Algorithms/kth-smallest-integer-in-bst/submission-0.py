# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def f(node, res):
            if not node: return

            f(node.left, res)
            if len(res)<k: 
                res.append(node.val)
                f(node.right, res)
        f(root, res)
        return res[-1]
