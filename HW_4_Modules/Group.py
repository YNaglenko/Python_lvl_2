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
        self.students = []

    def __str__(self):
        txt = "Group: {}, {} - {} \n".format(self.group_name, self.start_year, self.grad_year)
        if len(self.students) == 0:
            txt += "No students in this group"
        else:
            i = 1
            for stud in self.students:
                txt += str(i) + ". " + str(stud) + "\n"
                i += 1
        return txt

    def add_stud(self, student):
        try:
            if len(self.students) >= 10:
                raise GroupOverLimit(student)  # Виключення "переліміт групи"
            else:
                self.students.append(student)
                print("Student added successfully: {} {}".format(student.name, student.surname))
        except GroupOverLimit as err:
            print(err)

    def del_stud(self, surname, name):
        for student in self.students:
            if surname == student.surname and name == student.name:
                print("Deleted " + str(student))
                self.students.remove(student)
        return "Student deleted successfully"

    def search_by_surname(self, surname):
        found_item = None
        for student in self.students:
            if surname == student.surname:
                found_item = student
        return found_item
