class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, cols, origCol = len(image), len(image[0]),image[sr][sc]
        def traverse(sr,sc):
            if(not(0<=sr<row and 0<=sc<cols)) or origCol != image[sr][sc]:
                return
            image[sr][sc] = newColor
            [traverse(sr+x,sc+y) for x,y in ((0,1),(1,0),(-1,0),(0,-1))]
        if origCol != newColor:
            traverse(sr,sc)
        return image