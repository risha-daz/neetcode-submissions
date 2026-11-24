# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def f(res, node):
            if not node: return
            f(res, node.left)
            res.append(node.val)
            f(res, node.right)
        f(res, root)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True