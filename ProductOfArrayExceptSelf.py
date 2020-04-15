"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List

class Solution:
    def productExceptSelf_ConstantSpace(self, nums: List[int]) -> List[int]:
        list_size: int = len(nums)
        answer: List[int] = [1] * list_size  # Running Product of all elements to its left
        for i in range(0, list_size):
            if i == 0:
                answer[i] = nums[i]
            else:
                answer[i] = nums[i] * answer[i-1]
        right_product: int = 1
        for i in range(list_size-1, -1, -1):
            if i == list_size-1:
                answer[i] = answer[i-1]
            elif i == 0:
                answer[i] = right_product
            else:
                answer[i] = answer[i-1] * right_product
            right_product = right_product * nums[i]
        return answer
    
    def productExceptSelf_ExtraSpace(self, nums: List[int]) -> List[int]:
        list_size: int = len(nums)
        left_product: List[int] = [1] * list_size  # Running Product of all elements to its left
        right_product: List[int] = [1] * list_size # Running Product of all elements to its right
        for i in range(0, list_size):
            if i == 0:
                left_product[i] = nums[i]
            else:
                left_product[i] = nums[i] * left_product[i-1]
        for i in range(list_size-1, -1, -1):
            if i == list_size-1:
                right_product[i] = nums[i]
            else:
                right_product[i] = nums[i] * right_product[i+1]
        # Compute actual result
        for i in range(0, list_size):
            if i == 0:
                nums[i] = right_product[i+1]
            elif i == list_size - 1:
                nums[i] = left_product[i-1]
            else:
                nums[i] = left_product[i-1] * right_product[i+1]
        return nums
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return self.productExceptSelf_ExtraSpace(nums)
        return self.productExceptSelf_ConstantSpace(nums)
        
