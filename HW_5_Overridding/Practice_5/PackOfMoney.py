class PackOfMoney:
    def __init__(self):
        self.dict_pack = {}

    def __str__(self):
        res_txt = "PackOfMoney ["
        for d in self.dict_pack.keys():
            res_txt += str(d) + ":" + str(self.dict_pack[d]) + " "
        res_txt += "]"
        return res_txt

    def add_bill(self, denomination, quantity):
        if denomination in self.dict_pack:
            self.dict_pack[denomination] = self.dict_pack[denomination] + quantity
        else:
            self.dict_pack[denomination] = quantity

    def get_total(self):
        total_sum = 0
        for d in self.dict_pack:
            total_sum += d * self.dict_pack.get(d)
        return total_sum

    def __add__(self, other):
        for d in other.dict_pack.keys():
            quantity = other.dict_pack[d]
            self.add_bill(d, quantity)
        return self

    def __eq__(self, other):
        return self.get_total() == other.get_total()

    def __ne__(self, other):
        return self.get_total() != other.get_total()

    def __gt__(self, other):
        return self.get_total() > other.get_total()

    def __lt__(self, other):
        return self.get_total() < other.get_total()

    def __ge__(self, other):
        return self.get_total() >= other.get_total()

    def __le__(self, other):
        return self.get_total() <= other.get_total()
