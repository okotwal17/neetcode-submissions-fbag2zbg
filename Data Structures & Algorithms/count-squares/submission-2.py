class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = 1 + self.points.get(tuple(point), 0)

    def count(self, point: List[int]) -> int:
        numSquares = 0 
        for k, v in self.points.items():
            x1, y1, = point
            x2, y2 = k #Some other point
            if x1 == x2 or y1 == y2:
                continue
            point3, point4 = (x1, y2), (x2, y1)
            if point3 in self.points and point4 in self.points:
                numSquares += (v * self.points[point3] * self.points[point4])
        return numSquares
        
"""
Find one point with the same x coordinate, one point with the same y coordinate. 
Find last point with the same y coordinate as the first point and same x coordinate of the last point. 

Iterate throguh the points, and we then have our current point + this other random point

Say our point is (x1, y1) and other point is at (x2, y2)

Is there a point at (x1, y2) and is there a point at (x2, y1)?

If there is, thats a square. x

"""