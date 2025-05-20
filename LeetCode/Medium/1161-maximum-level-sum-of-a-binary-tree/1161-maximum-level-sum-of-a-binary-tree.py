#DFS 
#TC: O(n)
#SC: O(h)

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
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        larg = max(res)
        l = res.index(larg)
        return l+1

#BFS 
#TC: O(n)
#SC: O(h)
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
        
