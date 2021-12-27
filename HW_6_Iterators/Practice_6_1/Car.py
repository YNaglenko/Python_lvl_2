class CarIterator:
    def __init__(self, list_car):
        self.list_car = list_car
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_car):
            raise StopIteration
        else:
            tmp_car = self.list_car[self.index]
            self.index += 1
        return tmp_car


class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return "Car [model = {}, price = {}]".format(self.model, self.price)

