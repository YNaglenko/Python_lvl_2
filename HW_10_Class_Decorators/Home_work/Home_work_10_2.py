def str_add_left(add_from_left):
    def str_decorator(func):
        def new_function(*arg, **name_args):
            result = str(add_from_left) + " " + str(func(*arg, **name_args))
            return result
        return new_function
    return str_decorator


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    @str_add_left("Something_to_add")
    def __str__(self):
        return "Cat [name={}, age={}, color={}]".format(self.name, self.age, self.color)


newCat = Cat("Murzilka", 2, "red")
print(newCat)
