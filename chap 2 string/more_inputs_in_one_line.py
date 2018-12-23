#input more than one input in one line
name,age= input("enter your name and age(separated by space)").split()  #.split splits the string in specific separator and returns a list
print(name)
print (age)
#during giving name and age,a space will be provided into name and age,other wise it will be error,swaraj19 will not be accepted,swaraj 19 is correct
nm,ag=input("enter your name and age(separated by comma)").split(",")
print(nm)
print(ag)
# here space not required,you need to use a comma b/w name age
