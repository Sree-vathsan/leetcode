"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
          1(3)
         / \
        2(1)   3(0)
       / \     
      4(0)   5(0) 
"""
from typing import Tuple

class Solution:
    def __init__(self):
        self.result = 0
        
    def helper(self, node: TreeNode) -> int:
        """
        Returns depth
        """
        if not node:
            return 0
        if not node.left and not node.right:
            return 0
        this_diameter = depth_left = depth_right = 0
        if node.left:
            depth_left = self.helper(node.left)
            this_diameter += 1 + depth_left
        if node.right:
            depth_right = self.helper(node.right)
            this_diameter += 1 + depth_right
        this_depth = 1 + max(depth_left, depth_right)
        self.result = max(self.result, this_diameter)
        return this_depth
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.result
        
        
