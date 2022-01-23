# 1) Реализуйте метакласс, который обладает следующим функционалом: при
# его  использовании  в  файл  с  заранее  определенным  названием  нужно
# сохранить имя класса и список его полей.


class MetaLogger(type):
    def __new__(mcs, class_name, superclasses, class_attr):
        return type.__new__(mcs, class_name, superclasses, class_attr)

    def __init__(cls, class_name, parents, class_attr):
        filename = open("Meta_Logger" + ".txt", "a+")
        filename.write(class_name + ':\n')
        for attr in class_attr:
            filename.write(attr + '\n')
        filename.close()


class Cat(metaclass=MetaLogger):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Cat [name = {}, age = {}]".format(self.name, self.age)


class Car(metaclass=MetaLogger):
    def __init__(self, model, year):
        self.name = model
        self.year = year

    def __str__(self):
        return "Car [model = {}, year = {}]".format(self.name, self.year)


cat_one = Cat("Soniya", 2)
car_2000 = Car("Ford", 2015)

print(cat_one)
print(car_2000)
