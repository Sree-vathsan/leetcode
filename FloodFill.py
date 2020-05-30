"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
class Solution:
    def floodFillIter(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        max_row, max_col = len(image), len(image[0])
        src_color: int = image[sr][sc]
        q: List[Tuple[int]] = [(sr, sc)]
        while q:
            cr, cc = q.pop()
            if cr < 0 or cr >= max_row or cc < 0 or cc >= max_col or image[cr][cc] == newColor or image[cr][cc] != src_color:
                continue
            image[cr][cc] = newColor
            q.append((cr+1, cc))
            q.append((cr-1, cc))
            q.append((cr, cc+1))
            q.append((cr, cc-1))
        return image
        
    def floodFillRecur(self, image: List[List[int]], sr: int, sc: int, srcColor: int, newColor: int) -> List[List[int]]:
        dirs = [[0,1], [0,-1], [1, 0], [-1,0]]
        for d in dirs:
            nr, nc = sr + d[0], sc + d[1]
            if nr >= 0 and nr < len(image) and nc >= 0 and nc < len(image[1]) and image[nr][nc] == srcColor:
                image[nr][nc] = newColor
                self.floodFillRecur(image, nr, nc, srcColor, newColor)
        return image
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        srcColor: int = image[sr][sc]
        if srcColor == newColor:
            return image
        return self.floodFillIter(image, sr, sc, newColor)
