#data structure
# list > ordered collection of items
numbers = [1,2,3,4]
print(numbers[1])     # 1 print only 1st one

words = ["word1","word2",'word3']
print(words[:2])      # print 1st two items

mixed = [1,2,3,4,'five','six',2.3,None]
print(mixed[-1])      #print last one in the list

mixed[1:] = ['three','four']   # give position of item in the list in third brackett beside name of the list
print(mixed)          #if we want to change items inside the list         #breaks list

mixed[1:] = 'two'
print(mixed)          #it will replace item after 1 with 't' ; 'w' ; 'o'   # breaks string

mixed[1] = 1
print(mixed)          #it replace 1st item with 1