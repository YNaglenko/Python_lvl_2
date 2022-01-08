def str_decorator_class(cls):
    def __str__(self):
        return str(self.__class__.__name__)

    cls.__str__ = __str__
    return cls


@str_decorator_class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Kuzia", 6)
print(cat1)
