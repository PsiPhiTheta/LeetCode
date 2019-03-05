# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        out = []
        self.traverse(root, out)
        return out
    
    def traverse(self, root, out):
        if root:
            self.traverse(root.left, out)
            out.append(root.val)
            self.traverse(root.right, out)
