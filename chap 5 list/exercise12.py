# define func wich will take list containing  numbers AS input
# and return list containing squsre of every element:


#example:
#num=[1,2,3,4]
#squarelist=[1,4,9,16]

def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
numbers = list(range(1,11))
print(square_list(numbers))