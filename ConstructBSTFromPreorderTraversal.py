"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3339/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def bstFromPreorderIter(self, preorder: List[int]) -> TreeNode:
        root: TreeNode = TreeNode(preorder[0])
        stack = [root]
        index: int = 1
        while index < len(preorder):
            if preorder[index] < stack[-1].val:
                curr_node = TreeNode(preorder[index])
                stack[-1].left = curr_node
                curr_node = stack[-1].left
            else:
                while stack and preorder[index] > stack[-1].val:
                    node = stack.pop()
                curr_node = TreeNode(preorder[index])
                node.right = curr_node
            stack.append(curr_node)
            index += 1
        return root
    
    def findBisectPoint(self, preorder: List[int]) -> int:
        index: int = 1
        while index < len(preorder):
            if preorder[index] >= preorder[0]:
                return index
            index += 1
        return index
    
    def bstFromPreorderRec(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        ins_point = self.findBisectPoint(preorder)
        left_tree = self.bstFromPreorderRec(preorder[1:ins_point])
        right_tree = self.bstFromPreorderRec(preorder[ins_point:])
        curr_node = TreeNode(preorder[0], left_tree, right_tree)
        return curr_node
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # assert 1 == self.findBisectPoint([1,2,3])
        # assert 3 == self.findBisectPoint([10,9,8])
        # assert 1 == self.findBisectPoint([3,3,3])
        # assert 2 == self.findBisectPoint([5,1,7,10,12])
        # assert 1 == self.findBisectPoint([1,7,10,12])
        # assert 1 == self.findBisectPoint([7,10,12])
        # assert 1 == self.findBisectPoint([10,12])
        # return self.bstFromPreorderRec(preorder) if preorder else None
        return self.bstFromPreorderIter(preorder)
        
