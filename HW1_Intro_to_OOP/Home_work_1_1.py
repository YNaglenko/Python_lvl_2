# 1) Создайте пользовательский класс для описания товара (предположим,
# это задел для интернет-магазина). В качестве полей товара можете
# использовать значение цены, описание, габариты товара. Создайте пару
# экземпляров вашего класса и протестируйте их работу.


class Product:
    def __init__(self, description, price, weight):
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self):
        return "Good [description: {}, price: {}, weight {}]".format(self.description, self.price, self.weight)


new_good_1 = Product("Phone", 250.75, 0.15)
new_good_2 = Product("PC", 2450.00, 5.9)
new_good_3 = Product("Notebook", 4700.00, 2.5)

print(new_good_1)
print(new_good_2)
print(new_good_3)

new_good_2.price = 100.00
print(new_good_2)
