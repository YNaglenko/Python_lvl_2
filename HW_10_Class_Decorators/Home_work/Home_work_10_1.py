# 1) Создайте  декоратор,  который  зарегистрирует  декорируемый  класс  в
# списке классов.


class_array = []


def decorator_reg_class(cls):
    class_array.append(cls)
    return class_array


@decorator_reg_class
class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return "Cat [name = {}, age = {}, color = {}]".format(self.name, self.age, self.color)


@decorator_reg_class
class Car:
    def __init__(self, model, year, color, price):
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def __str__(self):
        return "Car [model = {},year ={}, color ={}, price ={}]".format(self.model, self.year, self.color, self.price)


for f in class_array:
    print(f)
