"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter
class Solution:
    """
    p = ab
    s = abcd
         ^ 
         
         a
         aaaa
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_dict_p = Counter(p)
        len_s, len_p = len(s), len(p)
        i = 0
        result: List[int] = []
        
        while i + len_p <= len_s:
            if i == 0:
                freq_dict_s = Counter(s[:len_p])
                if freq_dict_s == freq_dict_p:
                    result.append(i)
            else:
                freq_dict_s[s[i+len_p-1]] = freq_dict_s.get(s[i+len_p-1], 0) + 1
                if (result and i == result[-1] + 1 and s[i-1] == s[i+len_p-1]) or (freq_dict_s == freq_dict_p):
                    result.append(i)
                    
            if freq_dict_s[s[i]] == 1:
                del freq_dict_s[s[i]]
            else:
                freq_dict_s[s[i]] -= 1
            i += 1        
        return result
