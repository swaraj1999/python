# practicing functiion 
def last_char(name):
    return name[-1]     #this function to get last character of name

print(last_char("swaraj"))

def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"   #this function to check odd even number

print(odd_even(19))

#                   modifying odd_even function

def oddd_even(num):
    if num%2==0:
        return "even"
    return "odd"    #we are removing odd checking from if statement

print(oddd_even(19))

#                 again modifying odd_even func

def is_even(num):
    if num%2==0:
        return True
    return False     # if number is even return true

print(is_even(19))

#                 declaring odd_even function in pythonic way

def iss_even(num):
    return num%2==0  # if function is even return true

print(iss_even(19))
        