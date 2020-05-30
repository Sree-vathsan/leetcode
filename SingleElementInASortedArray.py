"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""
class Solution:
    """
    1,1,2
    1,2,2
    
    2,2,3,3,4
    2,3,3,4,4
    """
    def singleNonDuplicateBinarySearchExtraSpace(self, nums: List[int], nums_len: int) -> int:
        while nums:
            left, right = 0, len(nums) - 1
            mid = left + (right - left) // 2
            left_arr, right_arr = [], []
            if nums[mid] == nums[mid-1]:
                left_arr = nums[:mid-1] if mid - 1 >= 0 else []
                right_arr = nums[mid+1:] if mid + 1 < nums_len else []
            elif nums[mid] == nums[mid+1]:
                left_arr = nums[:mid] if mid >=0 else []
                right_arr = nums[mid+2:] if mid + 2 >= 0 and mid + 2 < nums_len else []
            else:
                return nums[mid]
            
            if left_arr and len(left_arr) % 2 == 1:
                nums = left_arr
            elif right_arr and len(right_arr) % 2 == 1:
                nums = right_arr
            else:
                return -1
            if nums and len(nums) == 1:
                return nums[0]
    
    def singleNonDuplicateBinarySearchNoExtraSpace(self, nums: List[int], nums_len: int) -> int:
        """
        inspiration: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/discuss/628036/Python-Binary-Search-O(logn)-explained
        """
        left, right = 0, nums_len
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid + 1 == nums_len:
                return nums[mid]
            elif nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        elif nums_len % 2 == 0:
            raise ValueError("Odd number of elements expected")
        return self.singleNonDuplicateBinarySearchNoExtraSpace(nums, nums_len)
        # return self.singleNonDuplicateBinarySearchExtraSpace(nums, nums_len)
        
                
            
