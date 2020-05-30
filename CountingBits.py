"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp: List[int] = [0] * (num+1)
        dp[1] = 1
        if num == 1:
            return dp
        i = 1
        while num >= 2**i:
            l, u = 2**i, 2**(i+1)
            for idx in range(l,u):
                dp[idx] = 1 + dp[idx-l]
                if idx == num:
                    return dp
            i += 1
        return -1
