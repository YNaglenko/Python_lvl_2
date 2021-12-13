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


while True:
    try:
        amt = (input("Enter product price: "))
        amt = float(amt)
        if amt < 0:
            raise NegativeValueError(amt)
        break
    except ValueError as err:
        print(err)
    except NegativeValueError as err:
        print(err, " ", err.amount)

print("The price is:", amt)
