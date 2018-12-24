# take name from user and print count of each word in name
name=input("enter your name user") #swaraj 


#name.count("s"),name.count(name[0])=1
#name.count("a"),name.count(name[1])=2

# using while loop
temp_variable = "" #store in temp
i=0
while i < len(name):
    if name[i] not in temp_variable: #name[i] is not present in temp variable
        temp_variable+= name[i]      #storing value of name i in temp
        print(f"{name[i] }:{name.count(name[i])}")
    i+=1 

# using for loop
temp =""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i] }:{name.count(name[i])}")
        temp += name[i]
