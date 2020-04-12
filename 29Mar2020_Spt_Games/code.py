# --------------
# #Code starts here

# #Function to read file
# def read_file(path):
    
#     #Opening of the file located in the path in 'read' mode
    
#     #Reading of the first line of the file and storing it in a variable
    
#     #Closing of the file
    
#     #Returning the first line of the file
    
    

# #Calling the function to read file

# #Printing the line of the file


# #Function to fuse message
# def fuse_msg(message_a,message_b):
    
#     #Integer division of two numbers
    
#     #Returning the quotient in string format
    
# #Calling the function to read file  

# #Calling the function to read file


# #Calling the function 'fuse_msg'


# #Printing the secret message 



# #Function to substitute the message
# def substitute_msg(message_c):
    
#     #If-else to compare the contents of the file
    
    
#     #Returning the substitute of the message
    
    

# #Calling the function to read file


# #Calling the function 'substitute_msg'


# #Printing the secret message



# #Function to compare message
# def compare_msg(message_d,message_e):
    
#     #Splitting the message into a list
    
    
#     #Splitting the message into a list
    
    
#     #Comparing the elements from both the lists
    
    
#     #Combining the words of a list back to a single string sentence
    
    
#     #Returning the sentence
    
    

# #Calling the function to read file


# #Calling the function to read file


# #Calling the function 'compare messages'


# #Printing the secret message


# #Function to filter message
# def extract_msg(message_f):
    
#     #Splitting the message into a list

    
#     #Creating the lambda function to identify even length words
    
    
#     #Splitting the message into a list
    
    
#     #Combining the words of a list back to a single string sentence
    
    
#     #Returning the sentence
    
    
# #Calling the function to read file


# #Calling the function 'filter_msg'


# #Printing the secret message


# #Secret message parts in the correct order
# message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


# # define the path where you 
# final_path= user_data_dir + '/secret_message.txt'

# #Combine the secret message parts into a single complete secret message


# #Function to write inside a file
# def write_file(secret_msg,path):
       
#     #Opening a file named 'secret_message' in 'write' mode


#     #Writing to the file


#     #Closing the file


# #Calling the function to write inside the file    


# #Printing the entire secret message


# #Code ends here


#####################################################

#Task 1 - Message Reading
##File path for the file 
file_path 

#Code starts here

def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()

    return sentence

sample_message = read_file(file_path)

print(sample_message)

#Task 2 - Message Fusion
#Code starts here

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

print(message_1)
print(message_2)

def fuse_msg(message_a, message_b):
    quotient = int(message_b) // int(message_a)

    return str(quotient)

secret_msg_1 = fuse_msg(message_1, message_2)

print(secret_msg_1)

#Task 3 - Message Substitution
#Code starts here

message_3 = read_file(file_path_3)

print(message_3)

def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'

    return sub

secret_msg_2 = substitute_msg(message_3)

print(secret_msg_2)

#Task 4 - Message Comparision
# File path for message 4  and message 5

#Code starts here

message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

print(message_4)
print(message_5)

def compare_msg(message_d, message_e):
    a_list = message_d.split(' ')
    b_list = message_e.split(' ')

    print(a_list)
    print(b_list)

    c_list = [i for i in a_list if i not in b_list]

    print(c_list)

    final_msg = " ".join(c_list)

    print(final_msg)

    return final_msg

secret_msg_3 = compare_msg(message_4, message_5)

print(secret_msg_3)



#Task 5 - Message Filter
#Code starts here

message_6 =read_file(file_path_6)

print(message_6)

def extract_msg(message_f):
    a_list = message_f.split(' ')

    print("This is A_LIST {0}", a_list)

    even_word = lambda x : len(x)%2==0

    b_list = list(filter(even_word, a_list))

    print("This is B_LIST {0}", b_list)

    final_msg = " ".join(b_list)

    return final_msg

secret_msg_4 = extract_msg(message_6)

print(secret_msg_4)

message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

#Code starts here

secret_msg = " ".join(message_parts)

def write_file(secret_msg, path):
    file = open(final_path, 'a+')
    file.write(secret_msg)
    file.close()

write_file(secret_msg, final_path)

print(secret_msg)

