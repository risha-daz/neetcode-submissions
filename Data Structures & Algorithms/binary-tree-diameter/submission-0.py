# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = [0]
        
        def maxDepth(node, h):
            if not node:
                return 0
            l = maxDepth(node.left, h+1)
            r = maxDepth(node.right, h+1)

            res[0] = max(res[0], h+l, h+r, l+r) 
            return 1 + max(l, r)
        maxDepth(root, 0)
        return res[0]
        

        
        
        
            

        