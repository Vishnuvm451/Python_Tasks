# #--------------- File Handling ---------------

# file_path ='C:/PGP/Python/demo.txt'
# reltive_path = 'demo.txt'



# file_1 = open(file_path,'r')      # assign a file in reading mode
# content_ = file_1.read()           # content of file is assigned to 'content_' variable
# print('File path',content_)
# file_1.close()

# file_2 = open(reltive_path,'r')           # assign a file in reading mode
# content_2 = file_2.read()                 # content of file is assigned to 'content_' variable
# print('Relative File path',content_2)     # print the content of file that we stored into 'content' variable 
# file_2.close()                            # closing the file

# print(' ')
# def read_file_path():
#     file_1 = open(reltive_path,'r')
#     content_ = file_1.read()
#     print('File path',content_)
#     print(type(content_))
#     file_1.close()
# read_file_path()


# print(' ')
# def read_relative_path():
#     file_2 = open(reltive_path,'r')
#     content_2 = file_2.read()
#     print('Relative File path',content_2)
#     print(type(content_2))
#     file_2.close()
# read_relative_path()


# print(' ')
# def read_file_line_by_line():
#     file_1 = open(reltive_path,'r')
#     content_3 = file_1.readline()
#     print('Relative File path line by line ',content_3)
#     print(type(content_3))
#     file_1.close()
# read_file_line_by_line()


# print(' ')
# def read_file_lines():
#     file_1 = open(reltive_path,'r')
#     content_4 = file_1.readlines()
#     print('File path lines one by one',content_4)
#     print(' ')
#     print('Lines one by one')
#     for line in content_4:
#         print(line)
#     print(type(content_4))
#     file_1.close()
# read_file_lines()




# ---------- Write a file ----------

write_path = 'student.txt'

def write_file_path():
    file = open(write_path,'w')     # make the file writable and if file is created if file not exists already .
    file.write('Hell\n')           
    file.write('Dude\n')           
    file.write('Well\n')           
    file.close()                    


write_file_path()



def write_name(get_input):

    file_1 = open(write_path,'w')
    file_1.write(get_input)
    file_1.close()

# write_name('hyy\n')

def append_name(get_input):

    file = open(write_path,'a')
    file.write(get_input)
    file.close()

# append_name('hello frnds ')


# generic function to append into a file - not dependable on other arguments 
# function works in arguments of that function

def append_data(file_get_path,data_to_add):

    file = open(file_get_path,'a')
    file.write(data_to_add)
    file.close()

append_data('append.txt','Appended 3rd time')


# do the same thing - open the file in appending mode and assing into 'file' variable
def append_data_(file_get_path,data_to_add):
    
    with open(file_get_path,'a')as file_:  
        file_.write(data_to_add)
        file_.close()

append_data_('append.txt','AIRTEL')


# learn to delete file 