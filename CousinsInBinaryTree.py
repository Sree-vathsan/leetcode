"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
from typing import Tuple
from functools import lru_cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        @lru_cache
        def getParentAndLevel(node: TreeNode, a: int, curr_level: int) -> Tuple[TreeNode, int]:
            if not node or (not node.left and not node.right):
                return (None, -1)
            if node.val == a:
                return (None, curr_level)
            if (node.left and node.left.val == a) or (node.right and node.right.val == a):
                return (node, curr_level + 1)
            left = getParentAndLevel(node.left, a, curr_level + 1)
            if left and left[1] != -1:
                return left
            else:
                right = getParentAndLevel(node.right, a, curr_level + 1)
                if right and right[1] != -1:
                    return right
            
        x_node, y_node = getParentAndLevel(root, x, 0), getParentAndLevel(root, y, 0)
        return x_node[1] == y_node[1] and x_node[0] != y_node[0]
