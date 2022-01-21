# 3) Реализуйте  свойство  класса,  которое  обладает  следующим
# функционалом:  при  установки  значения  этого  свойства  в  файл  с  заранее
# определенным  названием  должно  сохранятся  время  (когда  устанавливали
# значение свойства) и установленное значение.

import random
import time
from datetime import datetime


class Car:
    def __init__(self, model, price):
        self.model = model
        self._price = price

    def __str__(self):
        return "Car [model = {}, price = {}]".format(self.model, self._price)

    price = property()

    @price.getter
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        file = open("Price_Log" + ".txt", "a+")
        file.write("Price: " + str(value) + " changed at " + str(datetime.now()) + "\n")
        file.close()


my_car = Car("Audi", 2500)
print(my_car)

my_car.model = "VW"

for i in range(5):
    my_car.price = random.randint(5000, 25000)

    time.sleep(random.randint(0, 2))
    print(my_car)
