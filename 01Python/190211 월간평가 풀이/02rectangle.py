class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)

    def get_perimeter(self):
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.py.y))*2

    def is_square(self):
        return (self.p2.x - self.p1.x) == (self.p1.y - self.py.y)


if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    