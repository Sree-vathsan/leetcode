"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
from collections import Counter
class Solution:
    def isCheckInclusion(self, s: str, p: str) -> List[int]:
        freq_dict_p = Counter(p)
        len_s, len_p = len(s), len(p)
        i = 0
        while i + len_p <= len_s:
            if i == 0:
                freq_dict_s = Counter(s[:len_p])
                if freq_dict_s == freq_dict_p:
                    return True
            else:
                freq_dict_s[s[i+len_p-1]] = freq_dict_s.get(s[i+len_p-1], 0) + 1
                if freq_dict_s == freq_dict_p:
                    return True  
            if freq_dict_s[s[i]] == 1:
                del freq_dict_s[s[i]]
            else:
                freq_dict_s[s[i]] -= 1
            i += 1        
        return False
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return True if self.isCheckInclusion(s2, s1) else False
