"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
"""
class Solution:
    def moreCrispSolution(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a_idx, b_idx, a_len, b_len = 0, 0, len(A), len(B)
        result: List[List[int]] = []
        while a_idx < a_len and b_idx < b_len:
            a_s, a_e = A[a_idx]
            b_s, b_e = B[b_idx]
            if a_s <= b_s <= a_e or b_s <= a_s <= b_e or a_s <= b_e <= a_e or b_s <= a_e <= b_e:
                    result.append([max(a_s, b_s), min(a_e, b_e)])
            if a_e <= b_e:
                a_idx += 1
            else:
                b_idx += 1
        return result
    
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return self.moreCrispSolution(A, B)
