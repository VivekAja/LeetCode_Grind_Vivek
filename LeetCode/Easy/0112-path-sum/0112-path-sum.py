# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, summ):
            if root is None:
                return False
            summ +=root.val
            if root.left is None and root.right is None and summ == targetSum:
                return True
            return dfs(root.left, summ) or dfs(root.right, summ)
        return dfs(root, 0)

            