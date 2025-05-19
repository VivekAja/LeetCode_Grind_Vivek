class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    if not root:
        return 0

    # Start DFS from each node
    return dfs_from_node(root, targetSum) + \
        pathSum(root.left, targetSum) + \
        pathSum(root.right, targetSum)

def dfs_from_node(node, targetSum):
    if not node:
        return 0

    # Check if current node itself forms a valid path
    count = 1 if node.val == targetSum else 0

    # Continue path from the current node (left and right)
    count += dfs_from_node(node.left, targetSum - node.val)
    count += dfs_from_node(node.right, targetSum - node.val)

    return count
