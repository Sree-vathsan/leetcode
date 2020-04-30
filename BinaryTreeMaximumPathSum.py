"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = -inf
        
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        def maxPathSumRecur(currNode) -> int:
            if not currNode:
                return -inf
            if not currNode.left and not currNode.right:
                self.result = max(self.result, currNode.val)
                return currNode.val
            left = maxPathSumRecur(currNode.left)
            right = maxPathSumRecur(currNode.right)
            curr_sum = left + currNode.val + right
            self.result = max(self.result, left, right, left + currNode.val, right + currNode.val, currNode.val, curr_sum)
            return max(left + currNode.val, currNode.val + right, currNode.val) 
            
            
        maxPathSumRecur(root)
        return self.result
        
        
        
