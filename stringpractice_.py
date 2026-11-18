#------------- STRING -------------
string1 = 'uighwjgbnkneg][e[e]g[e]g[e]gfeg]'
string2 = 'python'
string3 = 'programming'

# print(string1)
print(string2)
print(string3)
print('--------------------------')
# by default print() statement prints a new line

print(string2 , end='&')
print(string3, end='&')
print(string2,string3)

# \t - newtab
# \n - newline

print('\t',string2,'\t',string3)


# --------------- CONCATENATION ---------------

s1 = 'ICT'
s2 = 'Academy'
s3 = 'Of'
s4 = 'Kerala'

print( s1 + s2 + s3 + s4 )
print( s1 , s2 , s3 , s4 )

combined_string = s1 + ' '+ s2 + ' ' + s3 +' ' + s4 
print(combined_string)

print('-----------------')

print(s1)                   # ICT
print(s1+s1+s1+s1+s1)       # ICTICTICTICTICT
print((s1 + ' ' )* 5)       # ICT ICT ICT ICT ICT
print((s1 + '\t' )* 5)      # ICT     ICT     ICT     ICT     ICT
# print((s1 + '\n' )* 5)

print('--------- INDEX ---------')
print(string3)
print(string3[0])
print(string3[5])
print(len(string3))

print(string1[-1])



#----------- 02/11/2026---------------
print('----------- 02/11/2026---------------')
str1 = 'TRIVANDRUM'
print(' ')
print('index position 6 or -4 of "TRIVANDRUM" is ',str1[6])

print('index 0 to 5 : ',str1[0:5])          # slicing "TRIVA" - index 0 to 5
print('index 6 to 10 : ',str1[6:10])         # slicing "DRUM" - index 6 to 10
# print(str1[10])                             # error coz : out of range 

print('index 4 to 7 : ',str1[4:7])          # slicing "AND" from "TRIVANDRUM" - index 4 to 7
print('print from starting to the end 0 TO END',str1[0:])          # print from starting to the end 0 TO END 
print('print from till 6',str1[:6])          # print from till 6

print('step up 2 positions - "TIADU" of "TRIVANDRUM"',str1[:9:2])       # step up 2 positions - "TIADU" of "TRIVANDRUM"
# print(str1[0:9:2]) - same output

print('step up 3 positions - "TVD" of "TRIVANDRUM"',str1[0:8:3])       # step up 3 positions - "TVD" of "TRIVANDRUM"

sr = 'bsyfsjbfhvnshvsjbvhsbsj vsjbvsjbnhgvsjbcjsbhsgbcvsnsihfsvbujbvkjbhbj'

print('to find the length of string',len(sr))   # to find the length of string
print('to find the last index position ',len(sr) -1) # to find the last index position 

txt = 'ALLA BOLELEO CHILLA BOLELEO !! KAMBALA BOLE '
if 'BOE' in txt :
    print('ALLA BOLELO IS PRESENT')
else :
    print('BINDAAS WON DAA')
text = "Heyy Guys I'm Learning python in ICT Academy of Kerala"
print(text[5::2]) # print from 5th index to end with 2 steps up 


print('revering string using slicing method',str1[::-1]) #     revering string using slicing method : str1 - "TRIVANDRUM is print backwards with steps 1 position - "MURDNAVIRT" " 
print('"TRIVANDRUM is print backwards with steps 2 position',str1[::-2]) #     in this case the str1 - "TRIVANDRUM is print backwards with steps 2 position - "MRNVR" "


# b = "Hello, World!"  - only printing H need to find
# print(b[0::-2]) 

# --------------- String Functions ---------------

print("--------------- String Functions ---------------")
print('str1 =',str1)
print('Convert string to lower case : ',str1.lower()) # Convert string to lower case
print('Convert string to upper case :',str1.upper()) # Convert string to upper case
print('Convert uppercase characters to lowercase & lowercase characters to uppercase :',str1.swapcase()) # Convert uppercase characters to lowercase and lowercase characters to uppercase
print('Return True if the string starts with the specified prefix, otherwise Return False :',str1.startswith('T')) # Return True if the string starts with the specified prefix, otherwise Return False . 
print('Starting letter only upper case rest of them are lower case :',str1.capitalize()) # Starting letter only upper case rest of them are lower case
b = " Hello, World! "
print('Removes the space in front and back',b.strip()) # removes the space in front and back - output : Hello, World!
print('Replace "H" with "J"',b.replace("H","J"))  # replace "H" with "J" - output : Jello, World! 
