#  Напишите программу, которая реализует функциональность считывания
# с  клавиатуры  стоимости  товара.  При  этом  стоит  учесть,  что  пользователь
# может ввести не цифры, а смесь цифр и букв или отрицательное число. При
# необходимости создайте пользовательское исключение и обработайте его
# (например, для отрицательных чисел).

class NegativeValueError(Exception):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def __str__(self):
        return "Positive amount expected, got negative"


class Product:
    def __init__(self, description, price, weight):
        self.description = description
        self.price = price
        self.weight = weight

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
            print(err, " ", err.amount,"CodeError:", prise_is_set_code)
        return prise_is_set_code

    def __str__(self):
        return "Product [description: {}, price: {}, weight {}]".format(self.description, self.price, self.weight)


test_product = Product("Phone", 1700, 105)
print(test_product)

while True:
    updated_price = input("Enter new price: ")
    ans = test_product.set_price(updated_price)
    if ans == 1:
        break
print(test_product)
