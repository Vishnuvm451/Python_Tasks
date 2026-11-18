#----------------PYTHON BASICS------------------------
# PYTHON DATATYPES 
# VARIABLES
#---------------------------------------------------

#Different types of DataTypes
print("Datatype of 'True' is",type(True))   #boolean
print('Datatype of {2026} is',type(2026.0))   #float

# This is a comment
# written in 
# more than just one line

# ------------------------------------------------
Name = str("Vishnu")
print ("Datatype of Name is" ,type(Name))   #string
Age = 21
print ("Datatype of Age is" ,type(Age))     #integer
x = float(20.546353520)
print(round(x,3))
print('--------------------------------------------')
# ------------------------------------------------
            # VARIABLES
# ------------------------------------------------
my_name = "Vishnu"
place = "Palakkad"
age = 21
gender = "Male"
mobile_number = 9544151773
email = "vishnu789451@gmail.com"
height = 168.0
# ------------------------------------------------

fred = 200
john = fred
print(john)
fred = 3
print(john)
print(fred)
# ------------------------------------------------
print('--------------------------------------------')
# Datatypes recheckimg 

print("Datatype of",my_name ,type(my_name))
print("Datatype of ",place ,type(place))
print("Datatype of ",age ,type(age))
print("Datatype of ",mobile_number ,type(mobile_number))
print("Datatype of ",email ,type(email))
print("Datatype of ",height ,type(height))
# ------------------------------------------------
print('--------------------------------------------')
print(f"My name is {my_name} . I am from {place}. I am {age} years Old . ") #1

# print("My name is " + my_name + "I am from " + place + "I am " + age + "Years old")  
# { we cannot directly call the 'int ' using cancatenation so instead we conert the 'int' to 'str'.}

print("My name is " + my_name + " I am from " + place + "I am " + str(age) + "Years old")  #2
print("My name is ", my_name, " I am from " , place , "I am ",age , "Years Old " ) #2
print(mobile_number)

print('--------------------------------------------')
#--------------------------- DATA TYPE CONVERSION -----------------------------------------

num1 = 234
num2 = 22.67

print("Data type of ",num1,type(num1))
print("Data type of ",num2,type(num2))

num3 = str(num2)
num4 = complex(num1)

print("Data type of ",num3,type(num3))
print("Data type of ",num4,type(num4))

num5 = str(777)
print("Data type of ",num5,type(num5))

# ------------------------------------------------

