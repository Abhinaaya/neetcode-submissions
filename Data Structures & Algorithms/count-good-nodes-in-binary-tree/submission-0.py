# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_val(root,max_till):
            count=0
            if not root:
                return 0
            if root.val>=max_till:
                count+=1
                max_till=root.val
            count+=count_val(root.left,max_till)
            count+=count_val(root.right,max_till)
            return count
        return count_val(root,float('-inf'))
        