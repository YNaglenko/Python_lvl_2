class NegativeValueError(Exception):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def __str__(self):
        return "Positive amount expected, got negative"


class ProductIterator:
    def __init__(self, list_goods):
        self.list_goods = list_goods
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_goods):
            raise StopIteration
        else:
            tmp_car = self.list_goods[self.index]
            self.index += 1
        return tmp_car


class Product:
    def __init__(self, description, price, weight):
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self):
        return "Product [description: {}, price: {}, weight {}]".format(self.description, self.price, self.weight)

    def set_price(self, new_price):
        prise_is_set_code = 0
        try:
            new_price = float(new_price)
            if new_price < 0:
                raise NegativeValueError(new_price)
            self.price = new_price
            prise_is_set_code = 1
        except ValueError as err:
            prise_is_set_code = -1
            print(err, "CodeError:", prise_is_set_code)
        except NegativeValueError as err:
            prise_is_set_code = -2
            print(err, " ", err.amount, "CodeError:", prise_is_set_code)
        return prise_is_set_code
