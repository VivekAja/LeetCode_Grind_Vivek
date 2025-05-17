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
        :rtype: List[List[int]]
        """
        self.allpaths = []
        def dfs(node, cp, cs):
            if not node:
                return False
            cp.append(node.val)
            cs+=node.val
            if node.left is None and node.right is None and cs == targetSum:
                self.allpaths.append(list(cp))
            if node.right:
                dfs(node.right, cp, cs)
            if node.left:
                dfs(node.left, cp, cs)
            cp.pop()

        dfs(root, [], 0)
        return self.allpaths