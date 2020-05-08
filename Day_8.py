class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        line = dx * coordinates[1][1] - dy * coordinates[1][0]
        for i in range(2, n):
            if line != dx * coordinates[i][1] - dy * coordinates[i][0]:
                return False
        return True
            
