from math import sqrt


class TriDescriptor:
    def __init__(self):
        pass

    def __get__(self, instance_self, instance_class):
        p = (instance_self.a + instance_self.b + instance_self.c) / 2.00
        area = sqrt((p * (p - instance_self.a) * (p - instance_self.b) * (p - instance_self.c)))
        return area

    def __set__(self, instance_self, value):
        raise AttributeError("field is only read only mode")

    def __delete__(self, instance_self):
        raise AttributeError("field can NOT be deleted")


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "Triangle [a = {}, b = {}, c={}]".format(self.a, self.b, self.c)

    area = TriDescriptor()


figure1 = Triangle(3, 4, 5)
print(figure1)
print(figure1.area)

del figure1.area

