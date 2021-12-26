class Rectangle:
    def __init__(self, a_side, b_side):
        self.a_side = a_side
        self.b_side = b_side

    def __str__(self):
        return "Rectangle [a = {}, b = {}]".format(self.a_side, self.b_side)

    def get_area(self):
        return self.a_side * self.b_side

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() == other.get_area()
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() != other.get_area()
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() > other.get_area()
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() < other.get_area()
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() >= other.get_area()
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() <= other.get_area()
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            self.b_side += (other.get_area() / self.a_side)
        return self

    def __iadd__(self, other):
        if isinstance(other, Rectangle):
            self.b_side += (other.get_area() / self.a_side)
        return self
