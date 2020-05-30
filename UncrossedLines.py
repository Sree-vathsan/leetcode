"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
"""
class Solution:
    """
        
        [1,3,7,1,7,5], B = [1,9,2,5,1]
        a. Preprocess
        [1,1,5]
        [1,5,1]
            0   1   2   3
        0   2   1   1   0
        1   2   1   1   0
        2   1   1   0   0
        3   0   0   0   0
        
        E, I = maxUncrossedLines([1,5] [1,5,1]), maxUncrossedLines([1,5], [5,1])
        maxUncrossedLines([5] [1,5,1]), maxUncrossedLines([5] [5,1]) -> 1
        maxUncrossedLines([5] [5,1]), maxUncrossedLines([5], [])
        
        if I >= E:
            I + 1
            
            0    1    2
        0   2    0    0  
        1   1    1    1  
        2   1    1    0
        
        A [1,4,2], B = [1,2,4]
        
        dp[i][j] = max(1 + dp[i+1][k+1], dp[i+1][j]) if A[i] in B[j:] and k is the index in B
        else
        dp[i][j] = dp[i+1][j]
        
        [2,2,5]
        [5,2,5,2]
            0   1   2   3   4
        0                   0
        1                   0
        2           1    0   0
        3   0   0   0   0   0
        
        A [1,4,2], B = [1,2,4]
        maxUncrossedLines([4,2] [2,4]), maxUncrossedLines([4,2], [1,2,4])
        
        """
    def _initDp(self, rows: int, cols: int) -> List[List[int]]:
        return [[0 for _ in range(cols)] for _ in range(rows)]
    
    def processMaxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        rows, cols = len(A), len(B)
        dp: List[List[int]] = self._initDp(rows+1, cols+1)
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                # dp[i+1][j]: ignoring A[i]
                # dp[i][j+1]: leave j to match with prior i and try matching forward
                # dp[i+1][j+1]: match with respective j
                if_matches = dp[i+1][j+1] + (1 if A[i] == B[j] else 0)
                dp[i][j] = max(dp[i+1][j], dp[i][j+1], if_matches)
        return dp[0][0]
    
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        # assert self._initDp(2,2) == [[0,0],[0,0]]
        # assert self._initDp(2,3) == [[0,0,0],[0,0,0]]
        return self.processMaxUncrossedLines(A, B)
        
        
