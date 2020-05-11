dirs = [[ 0, -1 ], 
        [ -1, 0 ], 
        [ 0, 1 ], 
        [ 1, 0 ]] 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or image[i][j] != color:
                return
            image[i][j] = newColor
            for d in dirs:
                dfs(i + d[0], j + d[1])
        dfs(sr, sc)
        return image
    
