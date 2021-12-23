class Human:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return "name = {}, surname = {}, age = {}, gender = {}".format(self.name, self.surname, self.age,
                                                                       self.gender)

