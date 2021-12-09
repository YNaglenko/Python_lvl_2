class Animal:
    def __init__(self, age, ration, color):
        self.age = age
        self.ration = ration
        self.color = color

    def get_voice(self):
        pass

    def __str__(self):
        return "age = {}, ration = {}, color = {}".format(self.age, self.ration, self.color)


class Cat(Animal):
    def __init__(self, age, ration, color, name, cat_type):
        super().__init__(age, ration, color)
        self.name = name
        self.cat_type = cat_type

    def get_voice(self):
        print("Meow")

    def __str__(self):
        return "Cat: " + super.__str__() + "name = {}, cat_type = {}".format(self.name, self.cat_type)


class Dog(Animal):
    def __init__(self, age, ration, color, name):
        super().__init__(age, ration, color)
        self.name = name

    def get_voice(self):
        print("Bow-Bow!")

    def __str__(self):
        return "Dod: " + super().__str__() + ", name = {}".format(self.name)


my_dog = Dog(5, "bones", "black", "Wishbone")

print(my_dog)
my_dog.get_voice()
