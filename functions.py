# # Defining a function 

# def abhinav(name):
#     print('Hello',name)


# # calling / invoking the function 
# abhinav('CC')

# # ---------------------------------------
# # function will have 
# # - function name : Mandatory
# # - input(s)
# # - Body of the function ( what the function actually does ) : Mandatory
# # - output


# # add 2 numbers 
# def sum_num(num1 , num2):
#     print('Sum = ',num1+num2)

# sum_num(2,3) # Sum =  5
# sum_num(2,3000) # o/p - Sum =  3002
# sum_num(342,True) # o/p - Sum =  343
# sum_num('HH','II') # concatenation happens ; o/p - Sum =  HHII
# sum_num(True,False) # o/p - Sum =  1
# sum_num(True,True) # o/p - Sum =  2


# # get input from user 



# def sum_func(n1,n2):
#     sum1 = n1+n2
#     print('sum = ',sum1)

# def user_func():
#     n1=int(input('n1 '))
#     n2=int(input('n2 '))
#     sum_func(n1,n2)

# user_func()



# # task 1
# print('Greetings ')
# def display_name(name):
#     print('Hi', name,'Good Afternoon\nHow are you ?')
    
# def get_name():
#     name = input('Enter Your Name :')
#     display_name(name)


# # get_name()
# # multiplication using While loop 

# def multip_func():
#     num=int(input('Enter num : '))
#     print('multiplication of ',num)
#     i=1
#     while(i<=10):
#         print(i,'x',num,' = ',i*num)
#         i=i+1
# multip_func()
    
# # multiplication using for loop 

# def multiplication_func():
#     num1 = int(input('Enter a num : '))
#     print('multiplication of ',num1)
#     for i in range(1,11):
#         print(i,'x',num1,' = ',i*num1)

# multiplication_func()




# # 5 score input 

# # sum        display
# # average    display
# # largest    display
# # smallest   display

# # 5 function define
# list_scores = (23,39,50,46,36)
# length=len(list_scores)

# def display_operations():
#     sum_of_scores()
#     total_marks=sum_of_scores()
#     print('Sum : ',total_marks)
#     average_of_scores(total_marks)
#     max_score()
#     min_score()

# def sum_of_scores():
#     # total = sum(list_scores)
#     total = 0
#     for i in list_scores:
#         total = total + i
#         i += 1
#     return total


# def average_of_scores(total_marks):
#     count = len(list_scores)
#     average_marks = total_marks/count
#     print('Average : ',average_marks)

# def max_score():
#     # using max() function

#     # max_score = max(list_scores)
#     # print('max score = ',max_score)

#     # using iteration
#     largest=list_scores[0]
#     for score in list_scores:
#         if score > largest:
#             largest= score
#     print('Largest :',largest)

# def min_score():
#     # using min() function

#     # min_score = min(list_scores)
#     # print('min score = ',min_score)

#     # using iteration
#     smallest=list_scores[0]
#     for score in list_scores:
#         if score < smallest:
#             smallest= score
#     print('Smallest :',smallest)



# display_operations()


# def check_even(i_num):
#     if i_num%2==0:
#         return True
#     else:
#         return False
# result = check_even(68)
# print(result)


# def calc_exp(num,exp=2):
#     print(num**exp)

# calc_exp(5)
# calc_exp(5,3)

# for i in range(1,6):
#     print(i, sep=',',end=' ')



def divide(num,den):
    result=num/den
    print(result)

# divide(40,5)
# divide('1234','5')
# divide(1234,0)


# exception handling 
# we write a specific criteria so that code flow is not interrupted.
# we write potential runtime error making code inside 'try' block
# and exception will caught by 'except' block



# rewriting the code with exception handling and displaying the error message 


def divide_new(num,den):
    try:
        result=num/den
        print(result)
    except Exception as e:
        print(f'There is an error : {e} ')
    
# divide_new(40,5)
# divide_new('1234','2')
# divide_new(1234,0)
# divide_new(55,5)



# rewriting the code with exception handling and displaying the appropriate error message 


def divide_new2(num,den):
    try:
        result=num/den
        print('result : ',result)
    except TypeError:
        print('Error Occured : Please make sure that you entered numbers ')
    except ZeroDivisionError:
        print('Error Occured : Please make sure that you give non zero value as denominator ')
    except Exception as e:
        print(f'There is an error occured : {e}')


divide_new2(40,5)
divide_new2('1234','a')
divide_new2(1234,0)
divide_new2(55,5)