# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: 
            return 0 
        else: 
            LHS = self.maxDepth(root.left) 
            RHS = self.maxDepth(root.right) 
            return max(LHS, RHS)+1 
