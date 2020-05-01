"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/

Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
 
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

 

Example 1:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0
Example 2:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
Example 3:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
 

Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].


"""
from typing import List, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidSequenceIter(self, root: TreeNode, arr: List[int]) -> bool:
        stack: List[Tuple[TreeNode, List[int]]] = [(root, arr)]
        while stack:
            curr_node, curr_arr = stack.pop(0)
            if curr_arr and curr_node.val == curr_arr[0]:
                if not curr_node.left and not curr_node.right and len(curr_arr) == 1:
                    return True
                if curr_node.right:
                    stack.append((curr_node.right, curr_arr[1:]))
                if curr_node.left:
                    stack.append((curr_node.left, curr_arr[1:]))
        return False
    
    def isValidSequenceRecur(self, root: TreeNode, arr: List[int]) -> bool:
        if not arr:
            return not root
        elif not root.left and not root.right:  # Leaf
            return len(arr) == 1 and root.val == arr[0]        
        else: # Non leaf
            if arr and root.val == arr[0]:
                left_tree_eval, right_tree_eval = False, False
                if root.left:
                    left_tree_eval = self.isValidSequenceRecur(root.left, arr[1:])
                if root.right and not left_tree_eval:
                    right_tree_eval = self.isValidSequenceRecur(root.right, arr[1:])
                return left_tree_eval or right_tree_eval
            else:
                return False
            
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            return False
        return self.isValidSequenceIter(root, arr)
        # return self.isValidSequenceRecur(root, arr)
        
        
