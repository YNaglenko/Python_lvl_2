# 3) Предположим,  в  классе  определен  метод  __str__,  который  возвращает
# строку  на  основании  класса.  Создайте  такой  декоратор  для  этого  метода,
# чтобы  полученная  строка  сохранялась  в  текстовый  файл,  имя  которого
# совпадает с именем класса, метод которого вы декорировали.

def str_to_file():
    def file_decorator(func):
        def new_function(*arg, **name_args):
            result = func(*arg, **name_args)
            file = open(str(func.__qualname__).split(".", 1)[0] + ".txt", "w")
            file.write(result)
            file.close()
            return result
        return new_function
    return file_decorator


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    @str_to_file()
    def __str__(self):
        return "Cat [name={}, age={}, color={}]".format(self.name, self.age, self.color)


newCat = Cat("Murzilka", 2, "red")
print(newCat)


