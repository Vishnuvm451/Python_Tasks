# 

# 1

# class Animal():
#     def eat(self):
#         print('eat')

# class Walks():
#     def walk(self):
#         print('walk')

# class Dog(Animal,Walks):
#     def bark(self):
#         print('Bow')

# dog = Dog()
# dog.bark()
# dog.eat()
# dog.walk()


# 2

# class Camera:
#     def take_photo(self):
#         print('Capturing photos')

# class Call:
#     def make_call(self):
#         print('Calling Friends')

# class Smart_phone(Camera,Call):
#     def internet(self):
#         print('Browsing Internet')

# phone = Smart_phone()
# phone.internet()
# phone.make_call()
# phone.take_photo()


# 3
# we creating 2 parent classes and 1 child class . in child class there  is only one method - change tv channel option . but we need to connecti_wifi and paly video .
# so we inherit methods from parent class . creating object inside child class . and calling the methods in parent class using child class object (tv is the child class object)
# syntax - child_class_object.methods_to_inherit() - at a time we can only call one method .abs


class MediaPlayer:
    def play_video(self):
        print('Playing video')

class InternetDevice:
    def connect_wifi(self):
        print('Connected to Wifi')

class SmartTv(MediaPlayer,InternetDevice):
    def change_channel(self):
        print('Changing TV Channel ')

tv = SmartTv()
tv.connect_wifi()
tv.change_channel()
tv.play_video()

