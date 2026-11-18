# username = input('Enter Your Username : ')
# password = input('Enter Password : ')
# age = int(input('Enter Age : '))
# height = input('Enter Height : ') # another method - height = float(input('Enter Height : ')) str to float
# print('Username :',username)
# print('Password :',password)
# print('Age :',age)
# print('Height :',height)

# height = float(height)      # we have to store dataype into the variable oyherwise conversion never happen - manual storing required
# print('Datatype of ', username ,type(username))
# print('Datatype of ', password ,type(password))
# print('Datatype of ', age ,type(age))
# print('Datatype of ', height ,type(height))

# Datatype of function input() - will always be string 
# convert data type - int(varaiable name)  eg : int(password)

# -------------- TASK 1 : PARAGRAPH FROM USER INPUTS --------------------

name = input('Enter Your Name : ')
dob = int(input('Enter your Birth Year : '))
place = input('Enter Place : ')
course = input('Enter Course : ')
college = input('Enter College Name : ')

print("------------------------------------------")

age = (2026 - dob)
print('Name :',name)
print('Age :',age)
print('Place :',place)
print('Course :',course)
print('College :',college)

print("------------------------------------------")

print('--- Self Introduction ---')
print("Hello Everyone ! I am", name ,"From" , place ,". I am ", age ,"Years Old\nStudied", course , "From" , college, ". And That's all about Myself ." )