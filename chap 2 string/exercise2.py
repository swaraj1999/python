#ask user to i/p 3 numbers,you have to print average using string formatting
x,y,z=(input("enter three number comma separated  ::")).split(",") #3 ,6, 4
# y=int(input("enter number 2 ::")) #6
# z=int(input("enter number 3 ::")) #4
# average=((x+y+z)/3)
print(f"average of two numbers{(int(x)+int(y)+int(z))/3}") #6.5