class Solution:
"""

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
