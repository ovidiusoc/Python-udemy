def add(*args):
    s = 0
    for i in args:
        s += i
    return s


print(add(1,2,3,4,5,6,7,9))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")


my_car = Car(make="Audi")
print(my_car.make)
print(my_car.model)
