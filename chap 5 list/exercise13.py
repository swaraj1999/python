# define a function which will reverse a list

# def reverse_list(l):            #1st process
#     return l.reverse()

# num = [1,23,4]
# print(reverse_list(num))

# def reversee_list(l):            #2nd process
#     return l[::-1]

# print (reversee_list(num))

def reverse_list(l):               #3rd process
    r_list = []
    for i in range(len(l)-1):
        popped_item = l.pop()    # pop items
        r_list.append(popped_item)  #add items at end
    return r_list
    

num = [1,2,4.8]
print(reverse_list(num))


