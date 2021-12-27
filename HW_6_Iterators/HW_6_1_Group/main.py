from HW_6_Iterators.HW_6_1_Group.Group import Group
from HW_6_Iterators.HW_6_1_Group.Student import Student

if __name__ == "__main__":
    # Створення екземлярів класів

    # Студент
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
    # my_group.add_stud(student_11)

    for t in my_group:
        print(t)
