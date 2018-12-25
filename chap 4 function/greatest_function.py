# to find the greatest number      #function inside function
def greater(a,b):
    if a>b:
        return a  
    return b           #it is finding the greater function in two number

def greatest(a,b,c):
    return greater(greater(a,b),c) #it will find among three

print(greatest(100000000,200,1200))
                                           #we can do it withoput calling greater ; its an example of function inside a function