"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
# import copy
class  MaximumSubarray:
    def greedy(self, nums: List[int]) -> int:
        curr_sum = answer = nums[0]
        for index in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[index], nums[index])
            answer = max(answer, curr_sum)
        return answer
    
    def dp(self, nums: List[int]) -> int:
        answer: int = nums[0]
        # dp: List[int] = copy.deepcopy(nums)
        dp = nums
        for index in range(1, len(nums)):
            if dp[index-1] > 0:
                dp[index] += dp[index-1]
            answer = max(answer, dp[index])
        return answer
    
    def maxSubArray(self, nums: List[int]) -> int:
        # return self.dp(nums)
        return self.greedy(nums)
