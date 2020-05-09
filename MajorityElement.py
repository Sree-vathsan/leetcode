"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
from collections import Counter
from typing import Dict

class Solution:
    
    def majorityElementExtraSpace(self, nums: List[int]) -> int:
        freq_dict: Dict[int, int] = Counter(nums)
        result = (-1, -1) # (num, freq)
        for k, f in freq_dict.items():
            result = (k, f) if f > result[1] else result
        return result[0]
    
    def majorityElementConstantSpace(self, nums: List[int]) -> int:
        """
        Credit: Linear Time Majority Voting Algo http://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html        
        """
        majority_elem = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                majority_elem = nums[i]
            elif nums[i] == majority_elem:
                count += 1
            else:
                count -= 1
        return majority_elem
    
    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElementConstantSpace(nums)
