# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        res = 0
        result= []
        queue = deque([root])

        while queue:
            level = len(queue)
            temp = 0
            for i in range(level):
                node = queue.popleft()
                #if i == level - 1:
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #res = max(res, temp)
            result.append(temp)

        larg = max(result)
        l = result.index(larg)
        return l+1
        