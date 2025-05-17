# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Calculate current prefix sum
            current_sum += node.val
            
            # Check if there's a valid path ending at this node
            paths = prefix_sum_count.get(current_sum - targetSum, 0)
            
            # Update prefix sum map with the current sum
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            
            # Recurse for left and right children
            paths += dfs(node.left, current_sum)
            paths += dfs(node.right, current_sum)
            
            # Backtrack: remove the current sum before returning to the parent
            prefix_sum_count[current_sum] -= 1
            
            return paths

        # Dictionary to store prefix sums
        prefix_sum_count = {0: 1}
        return dfs(root, 0)