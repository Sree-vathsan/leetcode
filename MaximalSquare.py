"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
from typing import Tuple
"""
3,4
sq = 3
0,1
"""
class Solution:

    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row_len, col_len, result = len(matrix), len(matrix[0]), 0
        dp: List[List[int]] = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]
        for i in range(1, 1+row_len):
            for j in range(1, 1+col_len):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    result = max(result, dp[i][j])
        return result ** 2
                            
                
        
        
            
