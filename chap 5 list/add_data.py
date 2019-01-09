# how to add data in list

#append method

fruits = ['grapes' , 'apple']
fruits.append('mango')       #append adds items at last
print(fruits)

#example
x=[]
x.append(1)
x.append(2)
print(x)

#insert method
fruits1=['mango','orange']
fruits1.insert(2, "grapes")  # we can add any position we want,2nd position
print(fruits1)

#concatinate two strings
y=fruits1+x
print(y)

# extend method
fruits.extend(fruits1)
print(fruits)
print(fruits1) #it actually extend list with elements of another list inside the list    #list inside list

#using append
fruits1.append(fruits)
print(fruits1)
print(fruits)  #elementb of list fruits will add with fruits1                            #we will get a complete list,no list inside list