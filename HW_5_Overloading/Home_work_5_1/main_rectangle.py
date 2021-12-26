from HW_5_Overloading.Home_work_5_1.Rectangle import Rectangle

if __name__ == "__main__":
    r_one = Rectangle(2, 0)
    print(r_one, "Area:", r_one.get_area())
    r_two = Rectangle(1, 3)
    print(r_two, "Area:", r_two.get_area())

    r_one + r_two
    print(r_one, "Area:", r_one.get_area())
    r_one += r_two
    print(r_one, "Area:", r_one.get_area())
