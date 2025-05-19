# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_path = 0


        def dfs(node, left_steps, right_steps):
            if not node:
                return
            
            # Update the maximum zigzag path length
            self.max_path = max(self.max_path, left_steps, right_steps)

            # If we go left, we continue a right zigzag (right_steps + 1)
            dfs(node.left, 0, left_steps + 1)
            # If we go right, we continue a left zigzag (left_steps + 1)
            dfs(node.right, right_steps + 1, 0)

        # Start DFS with initial 0 zigzag for both directions
        dfs(root, 0, 0)
        return self.max_path