from HW_5_Overridding.Home_work_5_1.Rectangle import Rectangle

if __name__ == "__main__":
    r_one = Rectangle(2, 1)
    print(r_one, "Area:", r_one.get_area())
    r_two = Rectangle(1, 3)
    print(r_two, "Area:", r_two.get_area())

    r_one + r_two
    print(r_one, "Area:", r_one.get_area())

    r_one += r_two
    print(r_one, "Area:", r_one.get_area())

    r_one * 2
    print(r_one, "Area:", r_one.get_area())

    r_three = Rectangle(2, 8)

    print(r_one > r_two)
    print(r_one < r_two)
    print(r_one >= r_two)
    print(r_one <= r_three)
