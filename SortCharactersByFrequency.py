"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        inv_freq: List[Set[int]] = [set()] * (len(s)+1)
            
        for k, v in freq_map.items():
            inv_freq[v] = inv_freq[v].union({k})
        
        return "".join(["".join(map(lambda a: "".join([a] * times), inv_freq[times])) for times in reversed(range(len(s)+1)) if inv_freq[times]])
