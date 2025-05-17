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

"""
python
import collections # Using deque for efficient stack operations

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum_iterative(self, root, targetSum):
        if root is None:
            return False

        # Stack stores tuples: (node, current_path_sum)
        stack = collections.deque([(root, root.val)])

        while stack:
            node, current_sum = stack.pop() # Use pop() for DFS behavior

            # Check if it's a leaf node
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    return True

            # Push children onto the stack with updated sums
            # Push right first so left is processed first (standard DFS order)
            if node.right:
                stack.append((node.right, current_sum + node.right.val))
            if node.left:
                stack.append((node.left, current_sum + node.left.val))

        # If the stack becomes empty and no path sum was found
        return False

# Example Usage (using the same tree as before):
# root ... (tree construction same as above)
sol = Solution()
print(sol.hasPathSum_iterative(root, 22)) # Output: True
print(sol.hasPathSum_iterative(root, 18)) # Output: True
print(sol.hasPathSum_iterative(root, 10)) # Output: False
print(sol.hasPathSum_iterative(None, 0)) # Empty tree edge case
print(sol.hasPathSum_iterative(None, 0)) # Output: False

Time Complexity: Both approaches visit each node at most once. For each node, we do constant time work (arithmetic, comparisons, stack push/pop). So, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:

Recursive: In the worst case (a skewed tree), the depth of the recursion can be O(N). This consumes O(N) space on the call stack. In the best case (a balanced tree), the depth is O(log N), leading to O(log N) space.
Iterative: In the worst case (a skewed tree), the stack can hold up to O(N) nodes. In the best case (a balanced tree), the maximum stack size is O(log N). So, the space complexity is O(N) in the worst case and O(log N) in the best case.
"""
