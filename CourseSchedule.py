"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
from collections import defaultdict
from typing import Dict, Set


class Solution:
    """
    Topological sort
    """
    
    def _constructInverseDepGraph(self, prerequisites: List[List[int]]) -> Dict[int, Set[int]]:
        dep_graph = defaultdict(set)
        for c, p in prerequisites:
            dep_graph[p].add(c)
        return dep_graph
    
    def _constructCountMap(self, numCourses: int, prerequisites: List[List[int]]) -> Dict[int, int]:
        count_map: Dict[int, int] = {}
        for i in range(numCourses):
            count_map[i] = 0
        for c, p in prerequisites:
            count_map[c] += 1
        return count_map
    
    def _getNoDepSet(self, course_dep_count_map: Dict[int, int]) -> Set[int]:
        no_dep_set: Set[int] = set(filter(lambda c: course_dep_count_map[c] == 0, course_dep_count_map.keys()))
        for c in no_dep_set:
            course_dep_count_map.pop(c)
        return no_dep_set
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if any(filter(lambda c: c[0] == c[1], prerequisites)):
            return False
        if not prerequisites:
            return True
        # inverse map: key:pre-req course and val:courses dependent on the pre-req 
        dep_graph: Dict[int, Set[int]] = self._constructInverseDepGraph(prerequisites)
        # key: course id and val num of pre-req pending
        course_dep_count_map: Dict[int, int] = self._constructCountMap(numCourses, prerequisites)
        while True:
            zero_dep_set = self._getNoDepSet(course_dep_count_map)
            if not zero_dep_set:
                break
            for pre_req in zero_dep_set:
                for c in dep_graph[pre_req]:
                    course_dep_count_map[c] -= 1
        return not course_dep_count_map
