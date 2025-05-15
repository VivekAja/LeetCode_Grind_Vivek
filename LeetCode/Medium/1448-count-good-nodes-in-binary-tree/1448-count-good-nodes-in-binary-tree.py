# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, largest = stack.pop()

            if largest <= node.val:
                good += 1
            largest = max(node.val , largest)

            if node.right: 
                stack.append((node.right, largest))
            if node.left: 
                stack.append((node.left, largest))

        return good
        #Time: o(n)
        #Space: o(n)