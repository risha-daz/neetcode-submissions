# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        bag = list()
        bag.append((0,root))
        curr_level = -1

        while bag:
            level, node = bag.pop(0)
            if node:
                bag.append((level+1, node.left))
                bag.append((level+1, node.right))

                if curr_level == level:
                    res[-1] = res[-1]+[node.val]
                else:
                    curr_level+=1
                    res.append([node.val])
        return res
