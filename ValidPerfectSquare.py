"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""
class Solution:
    def isPerfectSquareBinarySearch(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            mid_sq = mid ** 2
            if mid_sq == num:
                return True
            elif mid_sq > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        return self.isPerfectSquareBinarySearch(num)
        
