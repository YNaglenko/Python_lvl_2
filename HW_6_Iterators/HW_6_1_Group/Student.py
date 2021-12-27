from HW_4_Modules.Human import Human


class StudentIterator:
    def __init__(self, list_students):
        self.list_students = list_students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_students):
            raise StopIteration
        else:
            tmp_stud = self.list_students[self.index]
            self.index += 1
        return tmp_stud


class Student(Human):
    def __init__(self, name, surname, age, gender, university, faculty):
        super().__init__(name, surname, age, gender)
        self.university = university
        self.faculty = faculty

    def __str__(self):
        return "Student: " + super().__str__() + ", university = {}, faculty = {}".format(self.university, self.faculty)


