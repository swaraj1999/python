#syntax
#if condition
#   # code # if condition true execute
#   # code
age=int(input("enter your age : "))
if age>=14 :
    print("above 14")
#space before print func is important here ,otherwise indentation error
else :
    print("under 14")


#if  elif else statement

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60(250)
# above 60(200)
age =input("input your age ::::")
age =int(age)
#elif function is bascically working as else if function
if age==0 or age<0:
    print("you are baby")
elif 0<age<=3:
    print("ticket free")
elif 3<age<=10:
    print("ticket : 150")
elif 10<age<=60:
    print("ticket : 250")
else:
    print("ticket : 200")      