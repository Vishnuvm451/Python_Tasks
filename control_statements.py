# print('----- Control Statements -----')

# check whether the number > 50 

# number = int(input('Enter a Number : '))

# using if..else condition
# check number > 50 
# check number <= 50 

# if (number > 50) :
#     print(number,'is bigger than 50')
# else :
#     print(number,'is not greater than 50')

# if (number < 50) :
#     print(number,'is smaller than 50')


# ----------------------------------

# remainder = number%2
# print('Remainder = ',remainder)

# if (remainder==0):
#     print('Given number is Even')
# else:
#     print('Given number is Odd')


# print('End')

# ----------------------------------
# temp = float(input('Enter temperature in celsius : '))

# if(temp>350):
#     print('Dead Brohh ')
# else:
#     if(temp>=35):
#         print('Very Hot')
#     else:
#         if(temp>=25):
#             print('Warm Day')
#         else:
#             if(temp>=15):
#                 print('Cold Day')
#             else:
#                 if(temp<15):
#                     print('Freezing')

# print('--------------------------------')
# print(' ')
# if(temp>350):
#     print('Dead Brohh ')
# elif(temp>=35):
#     print('Very Hot')
# elif(temp>=25):
#     print('Warm Day')
# elif(temp>=15):
#     print('Cold Day')
# elif(temp<15):
#     print('Freezing')

# print('----- The End -----')



# print('----- Function value assign -----')

# def hello(name):
#     print("Hello !",name)

# name = input("Enter your name :")
# hello(name)


#---------------------------------------------------

# print('----- Iterative Statements -----')

# # for loop - used when no. of iterations are known
# # whilw loop - used when no. of iterations are known but stopping condition is known 

# # print your name 10 times 
# print('----- For Loop -----')
# for i in range(10):
#     print(i,'Vishnu')

# print('-------- using step operator --------')
# # range(start , end , step ) if step is not mentioned by default it take '1 step'
# for x in range(3,10,3):
#     print(x,'Vishnu')
# print('-------- using step operator backward --------')

# for x in range(30,10,-2):
#     print(x,'Vishnu')

# # print all odd numbers < 50
# print('--- odd numbers < 50 ---')

# for i in range(1,50,2):
#     print(i)

# # print all odd numbers between 20 - 50
# print('--- odd numbers between 20 - 50 ---')

# for i in range(21,50,2):
#     print(i)

print('----- While Loop -----')
# while loop will execute till the condition becomes false
num = 1
while(num < 10):
    print(num)
    num += 1

print('---- while loop : odd numbers < 50 ----')
temp = 1
while(temp < 50):
    print(temp)
    temp += 2

print('---- while loop : odd numbers between 20 - 50 ----')
num2 = 21
while(num2 < 50):
    print(num2)
    num2 += 2

print('--------- Logical operators in control flow statements ------------')

age = int(input('Enter age : '))
valid_id = input('Do you have any valid id ? (y/n) : ')
valid_id = valid_id.lower()
if(valid_id=='y'):
    valid_id = True
else:
    valid_id = False

print('Check Eligibility')

if(age>=18):
    if(valid_id):
        print('You are eligible')
    else:
        print('Not Eligible')
        print('Need a valuable ID ')
else:
    print('Not Eligible')
    print('Under 18')



# if(age >= 18 and valid_id==True):
#     print('Eligible to vote ')
# else:
#     print('Not Eligible')