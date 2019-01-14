# fromkeys                  # if we have 2 or more keys which have same values or name

#d = {'name' : 'unknown','age':'unknown'}

d=dict.fromkeys(['name','age'],'unknown')        # list,we can do tuple also
#d=dict.fromkeys(["abc" , 'unknown'])                   #a 'unknown' ,b 'unknown', c 'unknown'
#d=dict.fromkeys([range(1,11),'unknown'])                # 1 'unknown' ,2 'unknown'..........
#d=dict.fromkeys([name,age],[unknown,unknown])                  # name swaraj age 19 
print(d)                                         # if key not found it will give error
#print(d['name'])                                                 #to print name only        

# get method
d= {'name' : 'unknown','age':'unknown'}
print(d.get('names'))                          # if key not present it will show none,will not give error

# if none......>>false, else..........>true

#clear method

# d.clear()
print(d)                                         # clear the dictionary

# copy method

d1=d.copy()                # d1 and d are two separated dictionaries, check print  for diff of two case
#d1=d                        #it will not copy,same dictionary,if we pop,it will pop both d1 and d,not separate two dictionary
# try d1 = d, for same print downward
print(d1.popitem())
print(d)
print(d1 is d)



