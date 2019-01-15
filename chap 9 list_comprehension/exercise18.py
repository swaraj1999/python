# definer a function that takes list of string
# list containing reverse of string

# use list comprehension
def reverse_string(l):
    return [name[::-1] for name in l]                     # at first function to do then for loop

print(reverse_string(['abc','tuv','ggho']))


#normal way
# def rev_string(l):
#     new_list=[]
#     for name in l:
#         new_list.append(name[::-1])
#     return new_list
