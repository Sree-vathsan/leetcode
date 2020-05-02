"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""
from functools import reduce
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        def get_msd(p: int):
            msd: int = 0
            while p > 0:
                p = p >> 1
                msd += 1
            return msd
        
        if m == 0:
            return 0
        elif m == n:
            return m
        else:
            return 0 if get_msd(m) < get_msd(n) else reduce(lambda x, y: x & y, range(m,n+1))
        
