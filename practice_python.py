# ---------- IF CONDITION ------------

a = 100
b = 300

if b>a :
    print("a is greater or equal")
else :
    print("b  is greater")

# ---------- IF CONDITION ------------
#           Using Variables 

Attended_Class = True

if(Attended_Class== False):
    print(" Your are Absent")
else :
    print("Good Boy Present")


# -------- Get Input from From User ----------


# - used .lower() - Converts a string to lowercase
# eg : MONDAY / Monday  becomes - monday 
# - in - Checks whether a value exists in a collection [" "," "," "]
# - elif() - Checks another condition if the previous condition was false 
# - else() - Executes when none of the previous conditions is true


name=input("Enter your name : ")
#print(type(name))
print("Hello",name)
Day=input("What day is today :").lower()
if Day in["monday","tuesday","wednesday","thursday","friday"]:
    print("Class il podaa")
elif Day in ["saturday" ,"sunday"]:
    print("WOOW! URANGAMMM")
else:
    print("Invalid DAY")


print("-------------- IS / IS NOT -------------")

a = 5 
b = 6
c = a 

print("a is :", a)
print("b is :", b)
print("c is :", c)

print("c is a :",c is a)
print("c is b :",c is b)
print("c is not a :",c is not a)
print("c is not b :",c is not b)


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("x is : ",x)
print("y is : ",y)
print("z is : ",z)
print(x is z)
print(x is y)
print(x == y)

#----------------- LISTS  --------------------
print("------------ LISTS  --------------")

fruits_list = ['apple','banana','kiwi']
vegetables_list = ['tomato','potato','pumpkin','brinjal']

print('length of fruits_list items : ',len(fruits_list))
print('fruits_list',fruits_list)
print('lenth of vegetables_list items : ',len(vegetables_list))
print('vegetables_list',vegetables_list)

#----------------------------------------------------------

list1 = ["apple", "banana", "cherry"] # DATATYPE - STR
list2 = [1, 5, 7, 9, 3]    # DATATYPE - INT
list3 = [True, False, False]    # DATATYPE - BOOL
list4 = [True, 1, 'apple']  # DATATYPE - MIXED

print(list1)
print(list2)
print(list3)
print(list4)

print(type(list1))






name = "Vishnu"
for letter in name :
    print(letter , end="-")

import time

for i in range(10,0,-1) :
    print(i)
    time.sleep(1)
print("HAPPY BIRTHDAY")