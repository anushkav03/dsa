# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1 # current height plus one (the edge from curr to parent)

        dfs(root) # call dfs on root; traverse whole tree
        return self.diameter

        
