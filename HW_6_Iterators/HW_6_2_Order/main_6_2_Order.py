if __name__ == "__main__":
    # Створення товарів
    from HW_6_Iterators.HW_6_2_Order.Customer import Customer
    from HW_6_Iterators.HW_6_2_Order.Order import Order
    from HW_6_Iterators.HW_6_2_Order.Product import Product

    product1 = Product("Phone", 500.00, 0.15)
    product2 = Product("Notebook", 2150.00, 2.0)
    product3 = Product("Mp3", 300.75, 0.02)
    product4 = Product("HeadPhones", 200.00, 0.1)
    product5 = Product("Pad", 11300.00, 0.3)
    product6 = Product("PC", 8500, 5.0)
    product7 = Product("Router", 3500.79, 0.15)

    # Створення покупця
    customer1 = Customer("Bob", "Johnson", "38044124567")

    # Створення замовлення
    my_order = Order(customer1, product1)
    my_order.add_good(product2)
    my_order.add_good(product3)
    my_order.add_good(product4)
    my_order.add_good(product5)
    my_order.add_good(product6)
    my_order.add_good(product7)

    order2 = (my_order[:3])

    for f in order2:
        print(f)

    print("Test Iterator___")
    for i in my_order:
        print(i)




