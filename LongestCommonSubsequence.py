"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""


from functools import lru_cache

class Solution:
    """
        a   b   c   d   e   #
    a   3   2   2   1   1   0
    c   2   2   2   1   1   0
    e   1   1   1   1   1   0
    #   0   0   0   0   0   0
    s1: abcde
    s2: ace
    if s1[i] == s2[j]
        1 + dp[i+1][j+1] if i+1 and j+1 in bounds else 0
    else
        max(dp[i][j+1], dp[i+1][j+1]); handling bounds
    """
    @lru_cache(None)
    def longestCommonSubsequenceRecur(self, text1: str, text2: str, ind1: int, ind2: int) -> int:
        len_text1, len_text2 = len(text1), len(text2)
        if len_text1 == ind1 or len_text2 == ind2:
            return 0
        if text1[ind1] == text2[ind2]:
            return 1 + self.longestCommonSubsequenceRecur(text1, text2, ind1+1, ind2+1)
        else:
            return max(
                self.longestCommonSubsequenceRecur(text1, text2, ind1+1, ind2),
                self.longestCommonSubsequenceRecur(text1, text2, ind1, ind2+1)      
                      )
    
    def longestCommonSubsequenceDp(self, text1: str, text2: str) -> int:
        len_text1, len_text2 = len(text1), len(text2)
        result: int = [0] * len_text2
        
        for i in reversed(range(len_text1)):
            temp = result[:]
            for j in reversed(range(len_text2)):
                if text1[i] == text2[j]:
                    result[j] = 1 + temp[j+1]
                else:
                    result[j] = max(result[j], temp[j])
        return result[0]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.longestCommonSubsequenceDp(text1, text2)
        return self.longestCommonSubsequenceRecur(text1, text2, 0, 0) # Exceeds Time limits
        
        
