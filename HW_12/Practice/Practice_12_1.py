class CatCountMeta(type):
    def __init__(cls, class_name, super_classes, class_attr):
        cls.count = 0
        prev_init = cls.__init__

        def __init__(*args, **kwargs):
            cls.count += 1
            return prev_init(*args, **kwargs)

        cls.__init__ = __init__
        type.__init__(cls, class_name, super_classes, class_attr)


class Cat(metaclass=CatCountMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Cat [name = {}, age = {}]".format(self.name, self.age)


cat1 = Cat('Murka', 3)
cat2 = Cat('Murzik', 5)

print(Cat.count)
