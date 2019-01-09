#filter odd no even no
 
#list..[1,2,3,4,5,6]
#op>>[[1,3,5],[2,4,6]]

def filter(l): 
    odd_n = []
    even_n = []
    for i in l:
        if i%2==0:
            even_n.append(i)
        else:
            odd_n.append(i)
    output = [odd_n,even_n]
    return output
nums = [1,2,3,4,5,6,7,8,9,10]
print(filter(nums))
