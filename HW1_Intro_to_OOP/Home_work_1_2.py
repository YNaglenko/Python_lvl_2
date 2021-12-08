# 2)  Создайте  класс  «Покупатель».  В  качестве  полей  можете  использовать
# фамилию, имя, отчество, мобильный телефон и т.д.

class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return "Customer [name {}, surname: {}, phone: {}]".format(self.name,
                                                                   self.surname, self.phone)


my_customer = Customer("John", "Smith", "380441234578")

print(my_customer)
