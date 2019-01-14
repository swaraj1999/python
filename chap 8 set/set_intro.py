# set data type
# unordered collection of unique items
s={1,2,3,2,'swaraj'}
print(s)                 # we cant do indexing here like:: s[1]>>wrong here,UNORDERED

L={1,2,4,4,8,7,0,9,8,8,0,9,7}
s2=set(L)                 # removes duplicate,unique items only
print(s2)
s3=list(set(L))
print(s3)                   # set to list

# add data
s.add(4)
s.add(10)
print(s)

# remove method
s.remove(1)               #key not present in set,it will show error   && IF ONE KEY IS PRESENT SEVERAL TIME,IT WILL NOT REMOVE
print(s)

# discard method
s.discard(4)              # key not present in set,it will not set error
print(s)

# copy method
s1=s.copy()
print(s1)

#we cant store list tuple dictionary , we can store float,string


# we can use loop
for item in s:
    print(item)

# we can use if else
if 'a' in s:
    print('present')
else:
    print('false')


# union && intersection
s1={1,2,3}
s2={4,5,6}
union_set=s1|s2                 # union  |
print(union_set)

intersection_set=s1&s2          # intersection using &
print(intersection_set)
