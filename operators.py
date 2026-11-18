#--------------OPERATORS---------------------

# * Arithmetic Operators : + , - , * , / , % , ** , //
# * Conditional Operators : > , < , >= , <= , == , !=
# * Logical Operators : AND , OR , NOT 


#-----------------ARITHMETIC --------------------
print("--------------ARITHMETIC -------------")
num1 = 208
num2 = 3

sum = num1 + num2 
difference = num1 - num2 
multiply = num1 * num2 
division = num1 / num2
remainder = num1 % num2
exponent = num1 ** num2
floor_division = num1 // num2

print( "Sum of ", num1 , "+" , num2 ,"is : " , sum ,)
print("Difference between ", num1 , "and", num2 , "is :" , difference)
print("Products of", num1 , "and", num2 , "is :" , multiply)
print("We get remainder from", num1 , "and", num2 , "will be :" , remainder)
print("Exponent :" , exponent)
print("Floor division result from", num1 , "and", num2 , "will be :" , floor_division)

#----------------------------------------------------------

# this_year = int(input("Enter the Year :"))
# dob_year = int(input("Enter Birth Year :"))
# age = this_year - dob_year 

# print("Hello Buddy !  You are " , age , "Years Old ")

#----------------- RELATIONAL --------------------
print("-------------- RELATIONAL -------------")
print(num1 , '>' ,num2 , num1 > num2)
print(num1 , '<' ,num2 , num1 < num2)
print(num1 , '>=' ,num2 , num1 >= num2)
print(num1 , '<=' ,num2 , num1 <= num2)
print(num1 , '==' ,num2 , num1 == num2)
print(num1 , '!=' ,num2 , num1 != num2)

#------------------ LOGICAL ----------------------
print("------------- LOGICAL ------------")

# AND - all conditions should be true
# OR - any one condition needs to be true
# NOT - opposite

state1 = True
state2 = False
state3 = True
state4 = False

print("#------AND------")

print('state1 = True','; and','state2 = False',':',state1 and state2)
print('state1 = True','; and','state3 = True',':',state1 and state3)
print('state2 = False','; and','state4 = False',':',state2 and state4)

print("------#OR------")

print('state1 = True','; or','state2 = False',':',state1 or state2)
print('state1 = True','; or','state3 = True',':',state1 or state3)
print('state2 = False','; and','state4 = False',':',state2 or state4)

print("------#NOT------")

print('state1 = True :',not state1)
print('state2 = False :',not state2)
