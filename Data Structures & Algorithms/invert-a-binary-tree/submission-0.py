# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        bag = list()
        res = list()
        bag.append(root)

        while bag:
            i = bag.pop(0)
            temp = i.left
            i.left = i.right
            i.right = temp

            if i.left:
                bag.append(i.left)
            if i.right:
                bag.append(i.right)
        return root
        
