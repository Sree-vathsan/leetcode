"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import Dict
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse_map: Dict = dict()
        for i, v in enumerate(nums):
            if target - v in reverse_map:
                return [reverse_map[target - v], i]
            reverse_map[v] = i
        raise ValueError()
