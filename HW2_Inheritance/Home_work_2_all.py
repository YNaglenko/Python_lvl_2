# 1)  Создайте  класс,  описывающий  человека  (создайте  метод,  выводящий
# информацию о человеке).
# 2)  На  его  основе  создайте  класс  Студент  (переопределите  метод  вывода
# информации).
# 3)  Создайте  класс  Группа,  который  содержит  список  из  объектов  класса
# Студент. Реализуйте методы добавления, удаления студента и метод поиска
# студента  по  фамилии.  Определите  для  Группы  метод  __str__()  для
# возвращения списка студентов в виде строки.
# Клас Людина
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
        self.students.append(student)
        print("Student added successfully")

    def del_stud(self, surname, name):
        for student in self.students:
            if surname == student.surname and name == student.name:
                print("Deleted " + str(student))
                self.students.remove(student)
        return "Student deleted successfully"

    def search_by_surname(self, surname):
        count = 0
        txt = "Result of search: \n"
        for student in self.students:
            if surname == student.surname:
                count += 1
                txt += str(count) + ". " + str(student) + "\n"
        if count == 0:
            txt = 'No matches found by surname:{}'.format(surname)
        print(txt)


# Створення екземлярів класів

human_1 = Human("Bob", "Smith", 36, "M")
print(human_1)

student_1 = Student("Jack", "Johnson", 18, "M", "KPI", "FIOT")
print(student_1)

student_2 = Student("Nicole", "Woodworth", 19, "F", "KPI", "FIOT")
print(student_2)

student_3 = Student("Dmytro", "Kravchenko", 20, "M", "KPI", "IHF")
print(student_3)


my_group = Group("FIOT-001", 2010, 2015)
print(my_group)

# Додаємо студентів у групу
my_group.add_stud(student_1)
my_group.add_stud(student_2)
my_group.add_stud(student_3)
print(my_group)

# Видалення студента
my_group.del_stud("Johnson", "Jack")
print(my_group)

# Пошук студента
my_group.search_by_surname("Woodworth")
