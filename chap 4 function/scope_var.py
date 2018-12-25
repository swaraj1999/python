# scope of variable
x=5 # glpbal variable
def func():
    global x
    x=7 #local variable
    return x
#print(x)   # we cant do this,out of function
print(x)     #1st print global x
print(func())#2nd print local x
print(x)     #3rd print local x


# we cant print the local x into another funcself.


#instead of above
# print(func())   #local x
# print(x)        #global x
