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
class Solution:
    """
    [1,1,1,0,0,0]
    [1,1,1,-1,-1,-1] => max length of contiguous subarray whose sum equals k => k = 0

    
    """
    def findMaxLengthSolver(self, nums: List[int]) -> int:
        answer, running_sum, num_len = 0, 0, len(nums)
        nums = [-1 if nums[i] == 0 else 1 for i in range(num_len)]
        memo: Dict[int, int] = {0: -1}
        for index, val in enumerate(nums):
            running_sum += val
            if running_sum in memo:
                answer = max(answer, index - memo[running_sum])
            else:
                memo[running_sum] = index
        return answer
    
    def findMaxLength(self, nums: List[int]) -> int:
        return self.findMaxLengthSolver(nums)
