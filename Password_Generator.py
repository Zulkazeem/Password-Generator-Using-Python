#first import the necessary module
import random
import string

#determine the lenght of the password the user wants generated
Len_pass = int(input('Please enter the lenght of your password: '))

#make an array for the special characters
special_char = list(string.punctuation)

#the lowercase and uppercase alphabets have been imported from the string module
alpha = list(string.ascii_letters)

#the degits have also been imported from the string module
digits = list(string.digits)

combined_list = alpha + digits + special_char

#randomly select password from the combined list above using the random function
rand_pass = random.sample(combined_list, Len_pass)

password = "".join(rand_pass)

print("Your Newly Generated Password is " + password)
#print("And It Is Of Lenght " + len(int(password)))10
print("Thank You For Using Our Password Generator")



#section two, an alternate method

#determine the lenght of the password the user wants generated
"""Len_pass = int(input('Please enter the lenght of your password: '))

#make a list where the password will be generated from
password_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"

#use the random function to shuffle
rand_pass = random.sample(password_list, Len_pass)

password = "".join(rand_pass)

print("Your Newly Generated Password is " + password)
print("And It Is Of Lenght " + str(len(password)))
print("Thank You For Using Our Password Generator")"""


