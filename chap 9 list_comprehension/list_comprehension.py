# list comprehension
# with help of this we can make list in one line

# normal way
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

# using list comprehension
square2=[i**2 for i in range (1,11)]               # at first what to do,then range
print(square2)

# normal way
negative=[]
for i in range(1,11):
    negative.append(-1)
print(negative)

# using list comprehension
nega=[-1 for i in range (1,11)]           # 1st write what to append ,then for loop
print(nega)


names=['ddd','jjj','uuu']
#new_list=['d','j','u']
new_list=[name[0] for name in names]          # 1st write what to append,then for loop
print(new_list)