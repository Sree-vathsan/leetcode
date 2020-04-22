"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Perform binary search for each row and apply couple of optimizations along
        1. Short-circuit as soon as index=0 found
        2. When performing binary search limit within the min_col_index found so far.
        """
        row_len, col_len = binaryMatrix.dimensions()
        
        def leftMostColumnWithOnePerRow(rowIndex: int, min_col_index: int) -> int:
            """
            Perform binary search for the given row no stepping beyond the currently available min_col_index so far
            """
            low = 0
            high = col_len - 1 if min_col_index == col_len else min_col_index
            min_index: int = min_col_index + 1
            while (low <= high):
                mid = low + (high - low) // 2
                mid_val = binaryMatrix.get(rowIndex, mid)
                if mid_val == 0:
                    low = mid + 1
                else:  # it is 1, but we need leftmost 1
                    min_index = mid
                    high = mid - 1
            return min_index
        
        result: int = col_len
        for row in range(row_len):
            result = min(result, leftMostColumnWithOnePerRow(row, result))
            if result == 0:
                return result
        return result if result != col_len else -1
