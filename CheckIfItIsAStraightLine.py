"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""
from math import inf

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def getSlope(point1, point2):
            if point2[1] == point1[1]:
                return 0
            if point2[0] == point1[0]:
                return inf
            return (point2[1] - point1[1]) / (point2[0] - point1[0]) 
        
        if not coordinates or len(coordinates) <= 2:
            return True
        slope: float = getSlope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if slope != getSlope(coordinates[i-1], coordinates[i]):
                return False
        return True
