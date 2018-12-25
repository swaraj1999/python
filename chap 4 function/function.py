# function
# we need "def" keyword to define function

def add_two(num1,num2):
    return num1+num2
# adding two numbers
a = int(input("enter number...:  "))
b = int(input("enter number...:  "))
total=add_two(a,b)
print(total)                              #return sum of two numbers


#concatinate two strings
first_name = input("type 1st name :")
second_name = input("type 2nd name :")
print(add_two(first_name,second_name))     #return concatinate of two strings
   #
   # as it is dynamic prog lang,it can add two strings and two numbers as well