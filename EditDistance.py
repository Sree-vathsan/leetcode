"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
from collections import Counter
from typing import Dict
from math import inf


class Solution:
    """
        ""  r   o   s
    ""  0   1   2   3
    h   1   1   2   3   
    o   2   2   1   2           
    r               
    s
    e
    
    if w1[i] == w2[j]:
        dp[i][j] = dp[i-1][j-1]
    else:
        dp[i][j] = 1 + min(dp[i][j], dp[i-1][j], dp[i-1][j-1])
        
    
    """
    def minDistance(self, word1: str, word2: str) -> int:
        
        r, c = len(word1), len(word2)
        dp: List[List[int]] = [[inf for _ in range(c+1)] for _ in range(r+1)]
        
        for i in range(c+1):
            dp[0][i] = i
        for i in range(r+1):
            dp[i][0] = i
            
        for i in range(1, r+1):
            for j in range(1, c+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[r][c]
            
        
