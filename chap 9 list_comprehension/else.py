# list comprehension with if statement
#normal way
numbers=list(range(1,11))
#[1,2,3,4,5,6]
#even_nums=[2,4,6]
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)

# using list comprehension                               # for only if use if last
even_num=[i for i in range(1,11) if i%2==0]
print(even_num)
even_nums=[i for i in numbers if i%2==0]
print(even_nums)

#list comprehension with if else                        

# normal way
new_list=[]
for i in numbers:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-1)
print(new_list)

# list comp                                              # 1st cond, if state,2nd cond,else state
nw_list=[i*2  if (i%2==0) else -i for i in numbers]
print(nw_list)


# list in nested list

#example=[[1,2,3],[1,2,3],[1,2,3]]
# list comprehension
nested_comp=[[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

# normal way
# `new_list=[]
# for j in range(3):
#     new_list.append([1,2,3])`
