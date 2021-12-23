from HW_4_Modules.Human import Human


class Student(Human):
    def __init__(self, name, surname, age, gender, university, faculty):
        super().__init__(name, surname, age, gender)
        self.university = university
        self.faculty = faculty

    def __str__(self):
        return "Student: " + super().__str__() + ", university = {}, faculty = {}".format(self.university, self.faculty)

#1123
