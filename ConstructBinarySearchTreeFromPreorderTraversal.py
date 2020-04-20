"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List, Tuple

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def classify_left_right(partial_preorder: List[int]) -> Tuple[List[int], List[int]]:
            curr_root, l, r = partial_preorder[0], [], []
            for e in partial_preorder[1:]:
                if e < curr_root:
                    l.append(e)
                else:
                    r.append(e)
            return (l, r)
        
        def bstFromPreorderRec(preorder: List[int]) -> TreeNode:
            if not preorder:
                return None
            curr_root: int = preorder[0]
            if len(preorder) == 1:
                return TreeNode(curr_root)
            left_arr, right_arr = classify_left_right(preorder)
            this_node = TreeNode(curr_root)
            this_node.left = bstFromPreorderRec(left_arr)
            this_node.right = bstFromPreorderRec(right_arr)
            return this_node
        
        return bstFromPreorderRec(preorder)
        
        
