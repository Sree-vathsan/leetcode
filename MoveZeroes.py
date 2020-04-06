"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        [0,1,0,3,12]
        [1,0,0,3,12]
        Do not return anything, modify nums in-place instead.
        """
        curr: int = 0
        zero_ptr: int = 0
        while curr<len(nums):
            if nums[curr] != 0:
                if curr != zero_ptr:
                    nums[curr], nums[zero_ptr] = nums[zero_ptr], nums[curr]
                zero_ptr+=1
            curr+=1
