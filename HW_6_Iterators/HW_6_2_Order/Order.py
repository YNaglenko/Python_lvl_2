from HW_6_Iterators.HW_6_2_Order.Product import ProductIterator


class Order:
    def __init__(self, customer, good):
        self.customer = customer
        self.good = good
        self.list_goods = []
        self.list_goods.append(self.good)

    def add_good(self, good):
        self.list_goods.append(good)

    def remove_good(self, i):
        self.list_goods.remove(i - 1)

    def count_total_sum(self):
        total_price = 0
        for good in self.list_goods:
            total_price += good.price
        return total_price

    def __str__(self):
        i = 1
        z = str(self.customer) + "\n"
        for good in self.list_goods:
            z += str(i) + ". " + str(good) + "\n"
            i += 1
        return z + "Total: " + str(self.count_total_sum())

    def __len__(self):
        return len(self.list_goods)

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.list_goods):
                return self.list_goods[index]
            else:
                raise IndexError
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.list_goods) - 1 if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if start < 0 and stop >= len(self.list_goods):
                raise IndexError
            else:
                result = []
                for i in range(start, stop, step):
                    result.append(self.list_goods[i])
                return result
        raise TypeError()

    def __iter__(self):
        return ProductIterator(self.list_goods)
