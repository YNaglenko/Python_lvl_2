import numbers
import sys


class IsZeroAttribute(Exception):
    def __init__(self, a_side, b_side):
        super().__init__()
        self.a_side = a_side
        self.b_side = b_side

    def __str__(self):
        return "One of the sides with measures ({}, {}) cannot be 0".format(self.a_side, self.b_side)


class NegativeValueError(Exception):
    def __init__(self, a_side, b_side):
        super().__init__()
        self.a_side = a_side
        self.b_side = b_side

    def __str__(self):
        return "One of the sides with measures ({}, {}) cannot be negative".format(self.a_side, self.b_side)


class Rectangle:

    def __init__(self, a_side, b_side):
        try:
            if a_side == 0 or b_side == 0:
                raise IsZeroAttribute(a_side, b_side)
                return sys.exit()
            else:
                self.a_side = a_side
                self.b_side = b_side
            if a_side < 0 or b_side < 0:
                raise NegativeValueError(a_side, b_side)
        except IsZeroAttribute as err:
            print(err)
            return sys.exit()

        except NegativeValueError as err:
            print(err)

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
        else:
            NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Rectangle):
            self.b_side += (other.get_area() / self.a_side)
            return self
        else:
            NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            self.b_side = self.b_side * other
            return self
        else:
            NotImplemented
