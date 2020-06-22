from math import sqrt

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return (sqrt((coor2[0] - coor1[0]))**2 + (coor2[1] - coor1 [1])**2)

    def slope(self):
        return ((coor2[1] - coor1[1])/(coor2[0] - coor1[0]))

coor1 = (3,2)
coor2 = (8,10)

li = Line(coor1,coor2)

li.distance()

li.slope()