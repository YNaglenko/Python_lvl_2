from HW_6_Iterators.HW_6_1_Group.Student import StudentIterator


# Додана обробка вийнятків для кількості студентів
class GroupOverLimit(Exception):
    def __init__(self, student):
        super().__init__()
        self.student = student

    def __str__(self):
        return "Group is over limited. {} could not be added".format(self.student)


# Клас Група

class Group:
    def __init__(self, group_name, start_year, grad_year):
        self.group_name = group_name
        self.start_year = start_year
        self.grad_year = grad_year
        self.list_students = []

    def __str__(self):
        txt = "Group: {}, {} - {} \n".format(self.group_name, self.start_year, self.grad_year)
        if len(self.list_students) == 0:
            txt += "No list_students in this group"
        else:
            i = 1
            for stud in self.list_students:
                txt += str(i) + ". " + str(stud) + "\n"
                i += 1
        return txt

    def add_stud(self, student):
        try:
            if len(self.list_students) >= 10:
                raise GroupOverLimit(student)  # Виключення "переліміт групи"
            else:
                self.list_students.append(student)
                print("Student added successfully: {} {}".format(student.name, student.surname))
        except GroupOverLimit as err:
            print(err)

    def del_stud(self, surname, name):
        for student in self.list_students:
            if surname == student.surname and name == student.name:
                print("Deleted " + str(student))
                self.list_students.remove(student)
        return "Student deleted successfully"

    def search_by_surname(self, surname):
        found_item = None
        for student in self.list_students:
            if surname == student.surname:
                found_item = student
        return found_item

    def __iter__(self):
        return StudentIterator(self.list_students)

    # def __len__(self):
    #     return len(self.list_students)
    #
    # def __getitem__(self, index):
    #     if isinstance(index, int):
    #         if index >= 0 and index < len(self.list_students):
    #             return self.list_students[index]
    #         else:
    #             raise IndexError
    #     if isinstance(index, slice):
    #         start = 0 if index.start is None else index.start
    #         stop = len(self.list_students) - 1 if index.stop is None else index.stop
    #         step = 1 if index.step is None else index.step
    #         if start < 0 and stop >= len(self.list_students):
    #             raise IndexError
    #         else:
    #             result = []
    #             for i in range(start, stop, step):
    #                 result.append(self.list_students[i])
    #             return result
    #     raise TypeError()
