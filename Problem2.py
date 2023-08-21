#Time Complexity :O(n)
#Space Complexity :O(h)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None  or root==p or root==q:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left==None and right==None:
            return None
        elif left==None and right!=None:
            return right
        elif left!=None and right==None:
            return left
        else:
            return root
        
        

        

       

            