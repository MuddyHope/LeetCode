class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        count = -1
        dist = 20000000
        #boolean = False
        for i in range(len(points)):
            left,right = points[i][0],points[i][1]
            if (left == x or right == y):
                mindist = abs(left - x) + abs(right - y)
                if mindist < dist:
                    dist = mindist
                    count = i
            
        return count