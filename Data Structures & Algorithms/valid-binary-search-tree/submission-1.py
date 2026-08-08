# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inrange(low,high,node):
            if not node:
                return True
            if not (low<node.val<high):
                return False
            return (inrange(low,node.val,node.left) and inrange(node.val,high,node.right))
        return inrange(float('-inf'),float('inf'),root)

        

        