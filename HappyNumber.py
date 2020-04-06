"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
def reduce_n(n: int):
    total: int = 0
    while (n > 0):
        total += (n % 10) ** 2
        n = int(n / 10)
    return total

class Solution:
    def __init__(self):
        self.seen = set()
        
    def isHappyHelper(self, n: int) -> bool:
        if n == 1:
            return True
        if self.seen and n in self.seen:
            return False
        self.seen.add(n)
        return self.isHappyHelper(reduce_n(n))
        
    def isHappy(self, n: int) -> bool:
        return False if n == 0 else self.isHappyHelper(n)
