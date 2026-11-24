# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        bag = list()
        bag.append(root)

        while True:
            node = bag.pop()
            if ((p.val<=node.val and q.val>=node.val) or
                (p.val>=node.val and q.val<=node.val)):
                return node
            
            if node.left: bag.append(node.left)
            if node.right: bag.append(node.right)

        return root