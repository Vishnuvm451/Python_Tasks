# # ----------- SET -----------
# print('----------- SET -----------')

# # properties of a set
# # index is not stored in a set . given order is shuffled in output
# # set supports all datatypes - heterogenous datatype
# # repetation is not allowed - repeating values are not allowed (duplicates are deleted)
# # mutable


# # declaring methods

# set1 = {}             # it is a dictionary
# set2 = {'a','b','c'}
# set4 = {22,44,55,"a","b",True,22.0,55.8,'22'}
# set3 = set()


# roll ={1,2,3,4,5,6}
# roll_odd ={1,3,5}
# roll_even ={2,4,6}
# random ={1,5,9,4}


#  # add an element to the set
# random.add(2026)       
# print(random)

# # difference between set . element in random but not in roll_odd
# print(random.difference(roll_odd))

# # difference between set . element in roll_odd but not in random
# print(roll_odd.difference(random))

# # checking superset / subset  
# print(roll.issuperset(roll_odd))
# print(roll.issubset(roll_odd))

# # checking common elements in sets - intersection
# print(roll.intersection(roll_odd))

# # combining random set and roll_odd set . remove common values
# random.union(roll_odd) # expected o/p - {1,5,9,4,2026}
# print(random)

# # remove the given element from set
# random.discard(2026)
# print(random)

# # removes the first elemnt (popping) and no arguments can be given - can't specify which postion element to pop 
# random.pop()
# print(random)

# # removes an element we specify
# roll.remove(4)
# print(roll)
# print('--------------------')

# print(roll)
# print(random)

# # upadte / add
# roll.update(random)
# print(roll)

print('----------- DICTIONARY -----------')
# in a dictionary keys and values can be any datatype . 
# if duplicate keys - key will take the latest given value as value of that key 
# eg - { 1 : "one", 2 : "two" , 1 : "Yes " , 1 : "ICT"} - Here 1 key is repeating . latest value "ICT" is assigned to Key 1 -- {1 : "ICT"}


# dq = dict()
# d1 ={}
# d2 ={'key1' : 1, 8 : 12, True : "Yes", True : "Ayyoo"}
# print(type(d2))
# print(type(dq))
# print(type(d1))

# print(d2)
# # we can access values using key instead of index coz index is not stored in dictionary and tuples
# print(d2[True])
# print(d2[8])





my_dict = { "Name":"vishnu",
              "Age":21,
              "Course":"CS",
              "University":"Calicut",
              "Dictrict":"Palakkad"
}


# print('full dictionary')
# print(my_dict)

# print('keys only')
# print(my_dict.keys())

# print('values only')
# print(my_dict.values())

# # change values using .update() function 
# print(my_dict["university"])
# print(my_dict.update({"university":"KTU"}))
# print(my_dict)

# ------------------------------------------

# ask user to input info , store in same dictionary
# display the og dictionary 