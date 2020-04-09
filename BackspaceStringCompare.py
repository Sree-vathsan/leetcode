"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def extract_actual_string(self, raw_str: str) -> str:
        stack = []
        for c in raw_str:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    
    def extract_actual_string_no_extra_space(self, raw_str: str) -> str:
        index: int = 0
        while index < len(raw_str):
            if raw_str[index] == '#':
                if index == 0:
                    raw_str = raw_str[index+1:]
                else:
                    raw_str = raw_str[:index-1] + raw_str[index+1:]
                    index = index - 2 if index > 1 else index - 1
            else:
                index += 1
        return raw_str
        
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.extract_actual_string_no_extra_space(S) == self.extract_actual_string_no_extra_space(T)
