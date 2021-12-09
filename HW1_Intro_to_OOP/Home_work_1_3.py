# 3) Создайте  класс  «Заказ».  Заказ  может  содержать  несколько  товаров.
# Заказ должен содержать данные о пользователе, который его осуществил.
# Реализуйте  метод  вычисления  суммарной  стоимости  заказа.  Определите
# метод __str__() для корректного вывода информации о этом заказе.
# Клас Товар із задачі 1
class Product:
    def __init__(self, description, price, weight):
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self):
        return "Product [description: {}, price: {}, weight {}]".format(self.description, self.price, self.weight)


# Клас Покупець із задачі 2
class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return "Customer [name: {}, surname: {}, phone: {}]".format(self.name,
                                                                    self.surname, self.phone)


# Клас Замовлення
class Order:
    def __init__(self, customer, good):
        self.customer = customer
        self.good = good
        self.list_orders = []
        self.list_orders.append(self.good)

    def add_good(self, good):
        self.list_orders.append(good)

    def remove_good(self, i):
        self.list_orders.remove(i - 1)

    def count_total_sum(self):
        total_price = 0
        for good in self.list_orders:
            total_price += good.price
        return total_price

    def __str__(self):
        i = 1
        z = str(self.customer) + "\n"
        for good in self.list_orders:
            z += str(i) + ". " + str(good) + "\n"
            i += 1
        return z + "Total: " + str(self.count_total_sum())


# Створення товарів
product1 = Product("Phone", 500.00, 0.15)
product2 = Product("Notebook", 2150.00, 2.0)
product3 = Product("Mp3", 300.75, 0.02)
# Створення покупця
customer1 = Customer("Bob", "Johnson", "38044124567")

# Створення замовлення
my_order = Order(customer1, product1)

# Тест методу "загальна сума по замовленюю"
print(my_order.count_total_sum())

# Додавання другого товару у замовлення
my_order.add_good(product2)
print(my_order)

# Додавання третього товару у замовлення
my_order.add_good(product3)
print(my_order)
