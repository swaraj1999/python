
n=input("enter a number (more than one digit)") #12345
i = 0
total=0

#using while loop
while i<len(n):       #length=5
    total+=int(n[i])  #1+2+3+4+5=15 we need to do sum of digits
    i+=1
print(total)

#using for loop
# "123"
# int(num[0])=  1
# int(num[1])=  2
# int(num[2])=  3
# i=0 to 3
for i in range(0,len(num)):
    total+=int(num[i])
print(total)