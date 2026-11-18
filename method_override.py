# --------- METHOD OVERRIDE -----------

# animal is the parent class , dog and class is the child class . in method overriding the child class has the high priority .

# class Animal:
#     def move(self):
#         print('Animal Walks! ')

# class Frog(Animal):
#     def move(self):
#         print('Frog Jump! ')


# frog = Frog()
# frog.move()


# 1

# class Animal:
#     def sound(self):
#         print('Animal makimg sound')

# class Cat(Animal):
#     def sound(self):
#         print('Meow!')

# class Dog(Animal):
#     def sound(self):
#         print('Bow Bow')

# # cat =Cat()
# # cat.sound()
# dog = Dog()
# dog.sound()



# 2 

class Vehicle():
    def start(self):
        print('Vehicle is starting ')

class Car(Vehicle):
    def start(self):
        print('Car starts by using keys ')


class Electric_bike(Vehicle):
    def start(self):
        print('Bike starts by push button ')

bike = Electric_bike()
bike.start()

# car = Car()
# car.start()

