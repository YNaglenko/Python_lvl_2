# 3) Для класса Box напишите статический метод, который будет подсчитывать
# суммарный объем двух ящиков, которые будут его параметрами.

class Box:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def __str__(self):
        return "Box [h = {}, l = {}, w = {}]".format(self.height, self.length, self.width)

    def get_volume(self):
        return self.height * self.length * self.width

    @staticmethod
    def add_boxes(box1, box2):
        return box1.get_volume() + box2.get_volume()


first_box = Box(1, 2, 3)
second_box = Box(4, 5, 6)

print(first_box, "Volume:", first_box.get_volume())
print(second_box, "Volume:", second_box.get_volume())
total_volume = Box.add_boxes(first_box, second_box)

print("TotalVolume:", total_volume)


