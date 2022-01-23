class ToStr:
    def __str__(self):
        result = str(self.__class__.__name__) + "["
        for field in self.__dict__.keys():
            result += field + " = " + str(self.__dict__[field]) + ", "
        result = result[:-2]
        result += "]"
        return result


class MetaStr(type):
    def __new__(cls, class_name, superclasses, class_attr):
        superclasses = superclasses + (ToStr,)
        return type.__new__(cls, class_name, superclasses, class_attr)


class Cat(metaclass=MetaStr):
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Pumka', 12)
print(cat1)
