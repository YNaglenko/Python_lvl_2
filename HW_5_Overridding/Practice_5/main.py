from HW_5_Overridding.Practice_5.PackOfMoney import PackOfMoney

if __name__ == '__main__':
    a_pack = PackOfMoney()
    # a_pack.add_bill(20, 5)
    # print(a_pack)
    # total = a_pack.get_total()
    # print(total)
    #
    # a_pack.add_bill(100, 10)
    # print(a_pack)

    # total = a_pack.get_total()
    # print(total)

    b_pack = PackOfMoney()
    b_pack.add_bill(200, 5)
    a_pack.add_bill(200, 5)
    # a_pack.add_bill(100, 1)
    # print(b_pack)

    total = a_pack.get_total()
    # a_pack = a_pack + b_pack
    # print(a_pack)

    print(a_pack.get_total())
    print(b_pack.get_total())
    print(a_pack == b_pack, a_pack > b_pack)
