# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        child = set()

        for parents, children, lefty in descriptions:

            if parents not in nodes:
                nodes[parents] = TreeNode(parents)
            if children not in nodes:
                nodes[children] = TreeNode(children)
            child.add(children)

            if lefty:
                nodes[parents].left = nodes[children]
            else:
                nodes[parents].right = nodes[children]
        rootVal = (set(nodes.keys()) -child).pop()
        return nodes[rootVal]