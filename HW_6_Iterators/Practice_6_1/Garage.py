from HW_6_Iterators.Practice_6_1.Car import CarIterator


class Garage:
    def __init__(self):
        self.list_car = []

    def add_car(self, car):
        self.list_car.append(car)

    def __str__(self):
        res = "Garage [\n"
        for car in self.list_car:
            res += str(car) + "\n"
        res += "]"
        return res

    def __len__(self):
        return len(self.list_car)

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.list_car):
                return self.list_car[index]
            else:
                raise IndexError
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.list_car) - 1 if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if start < 0 and stop >= len(self.list_car):
                raise IndexError
            else:
                result = []
                for i in range(start, stop, step):
                    result.append(self.list_car[i])
                return result
        raise TypeError()

    def __iter__(self):
        return CarIterator(self.list_car)

