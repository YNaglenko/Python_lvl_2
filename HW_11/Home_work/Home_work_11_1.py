# 1) Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.

class ReadOnlyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __delete__(self, instance_self):
        raise AttributeError("fields in read only mode")

    def __set__(self, instance_self, value):
        raise AttributeError("fields in read only mode")


class Card:
    card_mask = ReadOnlyDescriptor("404259***37")

    def __str__(self):
        return "Card [ Number: {}]".format(self.card_mask)


newCard = Card()
print(newCard)

newCard.card_mask = "1111"
