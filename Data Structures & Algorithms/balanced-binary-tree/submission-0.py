# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def maxHeight(node):
            nonlocal res
            if not res: return False
            if not node: return 0

            l = maxHeight(node.left)
            r = maxHeight(node.right)

            if abs(l-r)>1: res = False
            return max(l,r) + 1
        maxHeight(root)
        return res




            