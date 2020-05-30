"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution:
    
    def removeKdigitsTimeLimitExceeded(self, num: str, k: int) -> str:
        """
        My brute force solution
        """
        def removeOnedigit(num: str) -> str:
            return str(min([int(num[:i]+num[i+1:]) for i in range(len(num))]))
            
        num_len = len(num)
        for _ in range(1,k+1):
            num = removeOnedigit(num)
        return num
    
    def removeKdigitsEfficient(self, num: str, k: int) -> str:
        """
        Logic: Maintain the invariant of keeping the stack in ascending order always
        Credit: https://stackoverflow.com/questions/28223580/how-to-get-the-least-number-after-deleting-k-digits-from-the-input-number
        """
        stack: List[int] = []
        for i in range(0,len(num)):
            this_num = int(num[i])
            while (k > 0 and stack and this_num < stack[-1]):
                stack.pop()
                k -= 1
            stack.append(this_num)
        if not stack:
            return "0"
        while k != 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == 0:
            stack.pop(0)
        return str("".join([str(i) for i in stack])) or "0"
        
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        elif k >= len(num):
            return "0"
        return self.removeKdigitsEfficient(num, k)
        
        
