# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos={value:i for i,value in enumerate(inorder)}
        def build(left,right,pre_id):
            if left>right:
                return None,pre_id
            root_val=preorder[pre_id]
            pre_id+=1
            root=TreeNode(root_val)
            mid=pos[root_val]
            root.left,pre_id=build(left,mid-1,pre_id)
            root.right,pre_id=build(mid+1,right,pre_id)
            return root,pre_id
        root,_=build(0,len(preorder)-1,0)
        return root
        