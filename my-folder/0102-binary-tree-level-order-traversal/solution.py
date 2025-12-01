# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curr_level = [root]
        next_level = []
        order = [[root.val]]
        while True:
            while curr_level:
                # pop
                node = curr_level.pop(0)
                # collect children at next level
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            # no more children at next level
            if not next_level:
                return order
            # else add level to return order
            order.append([node.val for node in next_level])
            curr_level = next_level
            next_level = []
