"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""
class Solution:
    def checkValidStringSimple(self, s: str) -> bool:
        left: int = 0
        right: int = 0
        str_len: int = len(s)
        for i in range(str_len):
            left += 1 if s[i] in '(*' else -1
            if left < 0:
                return False
            right += 1 if s[str_len-1-i] in '*)' else -1
            if right < 0:
                return False
        return True
        
        
    def checkValidString_verbose(self, s: str) -> bool:
        count: int = 0
        # Iterating string from left to right to match open paren
        for e in s:
            if e in '(*':
                count += 1
            else:  # ')'
                count -= 1
            if count < 0:
                return False
        if count == 0:  # else it can also be due to excess *
            return True
        # Iterating string from right to left to match closed paren
        count = 0
        for e in reversed(s):
            if e in '*)':
                count += 1
            else:  # '('
                count -= 1
            if count < 0:
                return False
        return True
    
    def checkValidString(self, s: str) -> bool:
        return self.checkValidStringSimple(s)
        # return self.checkValidString_verbose(s)
        
        
