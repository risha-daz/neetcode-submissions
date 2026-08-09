# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q): return True
        if (not p and q) or (not q and p): return False
        bag = list()
        bag.append((p, q))

        while bag:
            n1, n2 = bag.pop(0)
            if (n1.val != n2.val): return False

            if (n1.right and n2.right and
                n1.right.val == n2.right.val):
                    bag.append((n1.right, n2.right))
            elif n1.right or n2.right:
                return False

            if (n1.left and n2.left and
                n1.left.val == n2.left.val):
                    bag.append((n1.left, n2.left))
            elif n1.left or n2.left:
                return False
        return True            
                


        