class NegativeValueError(Exception):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def __str__(self):
        return "Input positive number"


while True:
    try:
        amt = float(input("Enter amount for withdrawal: "))
        if amt < 0:
            raise NegativeValueError(amt)
        break
    except ValueError as err:
        print("Wrong sum, enter amount again")
    except NegativeValueError as err:
        print(err, " ", err.amount)

print(amt)