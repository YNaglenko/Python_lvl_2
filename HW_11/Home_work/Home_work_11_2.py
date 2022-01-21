# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми  значениями,  кроме  целых  чисел.  Т.е.,  если  тому  или  иному  полю
# попытаться  присвоить,  например,  строку,  то  должно  быть  возбужденно
# исключение.

import numbers


class ItemDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, numbers.Integral):
            self.value = value
        else:
            raise ValueError("Item id must be Integer")


class Item:
    itemid = ItemDescriptor(-1)

    def __str__(self):
        return "Item [Item_id = {}]".format(Item.itemid)


new_item = Item()
print(new_item)

new_item.itemid = 1
new_item.itemid = 2.5
