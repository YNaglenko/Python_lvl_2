# 1) Создайте пользовательский класс для описания товара (предположим,
# это задел для интернет-магазина). В качестве полей товара можете
# использовать значение цены, описание, габариты товара. Создайте пару
# экземпляров вашего класса и протестируйте их работу.


class Product:
    def __init__(self, descr, price, weight):
        self.descr = descr
        self.price = price
        self.weight = weight
        self.item = {"descr": self.descr,
                     "price": self.price,
                     "weight": self.weight
                     }

    def __str__(self):
        txt = ""
        for key in self.item.keys():
            txt += key + ":" + str(self.item[key]) + " "
        return "Good [" + txt + "]"

    def set_price(self, new_price):
        self.item["price"] = new_price
        return "New price was set"

    def set_weight(self, new_weight):
        self.item["weight"] = new_weight
        return "New weight was set"

    def set_weight(self, new_descr):
        self.item["descr"] = new_descr
        return "New weight was set"


new_good_1 = Product("Phone", 250.75, 0.15)
new_good_2 = Product("PC", 2450.00, 5.9)
new_good_3 = Product("Notebook", 4700.00, 2.5)

print(new_good_1)
print(new_good_2)
print(new_good_3)

new_good_2.set_price(100.00)
print(new_good_2)

