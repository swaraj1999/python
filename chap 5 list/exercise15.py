# func
# [1,2,3,[1,2],[3,4]] , input
# count no of sub list >> 2
#use type()

def sub_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count+=1
    return count
num=[1,2,3,[1,2],[3,4]]
print(sub_count(num))