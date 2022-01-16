from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "Triangle [a = {}, b = {}, c={}, area={}]".format(self.a, self.b, self.c, self.area)

    def __getattr__(self, attr_name):
        if attr_name == "area":

            print("This is virtual field")
            p = (self.a + self.b + self.c) / 2.00
            area = sqrt((p * (p - self.a) * (p - self.b) * (p - self.c)))
        else:
            area = None
        return area


figure1 = Triangle(3, 4, 5)

print(figure1.area)
