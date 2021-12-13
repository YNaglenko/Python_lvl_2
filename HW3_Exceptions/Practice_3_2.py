# 1)  Создайте  класс,  описывающий  человека  (создайте  метод,  выводящий
# информацию о чeловеке).
# 2)  На  его  основе  создайте  класс  Студент  (переопределите  метод  вывода
# информации).
# 3)  Создайте  класс  Группа,  который  содержит  список  из  объектов  класса
# Студент. Реализуйте методы добавления, удаления студента и метод поиска
# студента  по  фамилии.  Определите  для  Группы  метод  __str__()  для
# возвращения списка студентов в виде строки.
# Клас Людина

# Додана обробка вийнятків для кількості студентів
class GroupOverLimit(Exception):
    def __init__(self, student):
        super().__init__()
        self.student = student

    def __str__(self):
        return "Group is overlimited. {} could not be added".format(self.student)


class Human:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return "name = {}, surname = {}, age = {}, gender = {}".format(self.name, self.surname, self.age,
                                                                       self.gender)


# Клас Студент
class Student(Human):
    def __init__(self, name, surname, age, gender, university, faculty):
        super().__init__(name, surname, age, gender)
        self.university = university
        self.faculty = faculty

    def __str__(self):
        return "Student: " + super().__str__() + ", university = {}, faculty = {}".format(self.university, self.faculty)


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


# Створення екземлярів класів
student_1 = Student("Jack", "Johnson", 18, "M", "KPI", "FIOT")
student_2 = Student("Nicole", "Woodworth", 19, "F", "KPI", "FIOT")
student_3 = Student("stud3", "test", 20, "M", "KPI", "IHF")
student_4 = Student("stud4", "test", 20, "M", "KPI", "IHF")
student_5 = Student("stud5", "test", 20, "M", "KPI", "IHF")
student_6 = Student("stud6", "test", 20, "M", "KPI", "IHF")
student_7 = Student("stud7", "test", 20, "M", "KPI", "IHF")
student_8 = Student("stud8", "test", 20, "M", "KPI", "IHF")
student_9 = Student("stud9", "test", 20, "M", "KPI", "IHF")
student_10 = Student("stud10", "test", 20, "M", "KPI", "IHF")
student_11 = Student("stud11", "test", 20, "M", "KPI", "IHF")

# Створення групи
my_group = Group("FIOT", 2010, 2015)

# Додаємо студентів у групу
my_group.add_stud(student_1)
my_group.add_stud(student_2)
my_group.add_stud(student_3)
my_group.add_stud(student_4)
my_group.add_stud(student_5)
my_group.add_stud(student_6)
my_group.add_stud(student_7)
my_group.add_stud(student_8)
my_group.add_stud(student_9)
my_group.add_stud(student_10)
my_group.add_stud(student_11)

print(my_group)


