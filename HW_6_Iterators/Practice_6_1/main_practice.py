from HW_6_Iterators.Practice_6_1.Car import Car
from HW_6_Iterators.Practice_6_1.Garage import Garage

if __name__ == "__main__":

    car_1 = Car("Audi A6", 12000)
    car_2 = Car("Honda Accord", 20000)
    car_3 = Car("Mercedes", 80000)
    car_4 = Car("BMW", 50000)
    car_5 = Car("AMG", 900000)
    print(car_1)
    gar1 = Garage()
    gar1.add_car(car_1)
    gar1.add_car(car_2)
    gar1.add_car(car_3)
    gar1.add_car(car_4)
    gar1.add_car(car_5)

    print(gar1)

    gar2 = (gar1[:3])

    for f in gar2:
        print(f)

    print("Check Iterator____")
    for car in gar1:
        print(car)
