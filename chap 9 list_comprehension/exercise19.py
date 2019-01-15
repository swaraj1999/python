# num to string
def num_string(l):
    return[str(i) for i in l if (type(i)==int or type(i)==float)]

print(num_string([True,False,[1,2,4],1,1.0,4]))                     # print only numbers 