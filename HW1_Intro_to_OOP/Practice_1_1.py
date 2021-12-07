class RectAng:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return "Rectangle [side_a = {}, side_b = {}]".format(self.side_a, self.side_b)

    def get_square(self):
        return self.side_a * self.side_b


my_figure = RectAng(3, 4)
print(my_figure.get_square())

print(my_figure)