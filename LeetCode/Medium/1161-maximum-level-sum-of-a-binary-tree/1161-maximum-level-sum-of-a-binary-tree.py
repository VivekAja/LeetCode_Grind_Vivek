# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []

        def dfs(node, level):
            temp = 0
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            else:
                res[level] += node.val
            #res.append(temp)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        larg = max(res)
        l = res.index(larg)
        return l+1