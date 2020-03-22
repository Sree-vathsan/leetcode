class Solution:
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
    def isValid(self, s: str) -> bool:
        stack: list = []
        valid_paren_dict: Dict = {")": "(", "}": "{", "]": "["}
        for current_char in s:
            if current_char in valid_paren_dict and stack and stack[-1] == valid_paren_dict[current_char]:
                stack.pop(-1)
            else:
                stack.append(current_char)
        return not stack
