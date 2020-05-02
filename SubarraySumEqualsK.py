"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum: int = 0
        memo: Dict[int, int] = {}
        result: int = 0
        
        for index in range(len(nums)):
            running_sum += nums[index]
            if running_sum == k:
                result += 1
            if running_sum - k in memo:
                result += memo[running_sum - k]
            memo[running_sum] = 1 + memo.get(running_sum, 0)
            
        return result
                
