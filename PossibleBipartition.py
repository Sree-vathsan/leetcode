"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
from collections import defaultdict
from typing import Dict, Set

class Solution:
    def __init__(self):
        self.colorMap = {}
        self.graph = defaultdict(set)
        
    def constructGraph(self, N: int, dislikes: List[List[int]]) -> Dict[int, Set[int]]:
        graph = defaultdict(set)
        for i in range(1, N+1):
            graph[i] = set()
        for s, d in dislikes:
            graph[s].add(d)
            graph[d].add(s)
        return graph
    
    def dfs(self, src: int, color: 0) -> bool:
        if src in self.colorMap:
            return self.colorMap[src] == color
        else:
            self.colorMap[src] = color
            color = ~color
            for adj_node in self.graph[src]:
                if not self.dfs(adj_node, color):
                    return False
        return True
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = self.constructGraph(N, dislikes)
        for node in self.graph:
            if node not in self.colorMap:
                if not self.dfs(node, 0):
                    return False
        return True
                
