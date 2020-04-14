"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
from typing import Tuple, List
class Solution:
    """
    [0,0,0,1,1,1]
    [-1,-1,-1,1,1,1]
    [-1,-2,-3,-2,-1,0]
    0: -1
    -1: 0
    -2: 1
    -3: 2
    len: 3 - 1 = 2
    len: 4 - 0 = 4
    len: 5 - (-1) = 6
    
    """
    def findMaxLength(self, nums: List[int]) -> int:
        n: int = len(nums)
        result: int = 0
        memo = {0: -1} # For the subarray that starts from index 0
        running_sum: int = 0
        nums = [e if e == 1 else -1 for e in nums] # Replace all 1 by -1
        for curr_index, e in enumerate(nums):
            running_sum += e
            if running_sum not in memo:
                memo[running_sum] = curr_index
            else:
                # already seen
                result = max(result, curr_index - memo[running_sum])
        return result
            
        
