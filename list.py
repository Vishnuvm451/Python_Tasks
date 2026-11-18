# List is a datatype used to store a collection of values
# it is a  combination of other datatypes (int , float , string , boolean )
# list can contain any datatype even list , tuple , set ...
# list can contain various types of data - Heterogenous.

print('---------- LIST ------------')

# #  list declaring

# # method 1
# last_name = ["Vishnu","Akash","Ajith"]
# print(type(last_name))          

# #  method 2
# name = [45,78.0,True,last_name]
# print(type(name))

# # method 3 
# # lst_name = list()
# # print(type(lst_name)) 

# print('# fetch values from list using index')
# print(name[-1])
# print(name[-2])
# print(name[0])
# print(name[1])
# print('# check datatype of value inside the list')
# print(type(name[1]))
# print(type(name[3]))
# print(type(name[2]))

# list1 = [1,2,5,7,3]
# print('list1:',list1)
# print(type(list1))
# list2 = [True , False , False]
# print('list2:',list2)
# print(type(list2))
# list3 = list1 + list2
# print(list3)
# print(type(list3))


# sorting ( ascending order )

l1 = [1,2,5,7,3]
l1.sort()
print('ascending order',l1)

# # sorting ( descending order ) give parameter - reverse = True
# l1 = [1,2,5,7,3]
# l1.sort(reverse=True)
# print('descending order',l1)
# print(' ')

n1 = ["Vishnu","Akash","Ajith"]
n1.sort()
print('asescending order',n1)

# n1 = ["Vishnu","Akash","Ajith"]
# n1.sort(reverse=True)
# print('descending order',n1)

l1.extend(n1) # values in n1 list is added to the end of l1 list - all values in n1 i added to each index seperately at end of l1
# [1, 2, 3, 5, 7, 'Ajith', 'Akash', 'Vishnu']
print(l1)

print('Count of Vishnu in list : ',n1.count("Vishnu"))

# n1.remove("Vishnu")
# print(n1)

l1.append(n1) # n1 list is added as last value of l1 . here last index is a list containing multiple values  ['Ajith', 'Akash', 'Vishnu']
print(l1)

l1.append(7)  # added 'n1' at end . but we can give only 1 argument at a  time 
print(l1)

print('original :',l1)
l1.reverse()
print('reverse :',l1)



print('no of 7 : ',l1.count(7))
print('no of "Vishnu" : ',l1.count("Vishnu"))
print('no of "vh" : ',l1.count('vh'))

print('l1 list : ',l1)
print('fetch no of items in a list')

print('length of items in l1 : ',len(l1))

print('last item in l1 : ',l1[-1]) 
print('------------------------')
print('before ',l1)

# l1.clear()

# print('after',l1)
# print(type(l1))


l1.insert(2,'A')
print('after  ',l1)

l1.pop(3)            # Remove and return item at index (default last).
print(l1)           #  l1.pop(3)  - removes index 3rd item 

l1.remove(3)        # remove item 3 from the list  - removes specific value
print(l1)

l1.remove(l1[1])        # remove item in l1[1] index position from the list 
print(l1)

print('---------- TUPLE ------------')

# tuple is a datatype used to store a collection of valuessince it is combination of other data types (int , bool , string , float) - derived datatype
# it contains various datatypes - heterogenous 

tuple1 = (1,'a',5.5)
tuple2 = ()
tuple3 = tuple()
list56 = ['a',23,False]
print(tuple1)

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print('tuple1[2]',tuple1[2])
print('type of tuple1[2]',tuple1[2],' is ',type(tuple1[2]))

print(tuple1.index(5.5)) 

print(tuple1.count('K'))


# once a tuple is created , we can't change / modify the tuple 
# List - Mutable           (can change / modify values )
# Tuple  - immutable       (can't change / modify values )

del(tuple2)
del(list56)
