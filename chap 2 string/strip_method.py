#this method is used to remove space and find and replace`
name="    swar    aj    "
dots="........." # tocheck the space
print(name+dots) #    swar  aj   .....

# lstrip method ...>>to remove space of left side of string
print(name.lstrip()+dots) #swar   aj   ......

# rstrip method ...>> to remove space of right side of string
print(name.rstrip()+dots) #     swar  aj.....

#strip method...>>to remove both lft and ri8 spave
print(name.strip()+dots) #swar   aj...

#replace method ...>>>to replace something with something else
print (name.replace(" ","")+dots) #swaraj.....
string="she is beautiful and she is good"
print(string.replace("is","was",1)) # she was beautiful and she is good ;replacing only 1st is

# find method...>> to find the position of word
print(string.find("is")) # 4,it wiil find 1st is
print(string.find("is",8)) # 25, it will find is after position 8
is_pos1 =string.find("is") #is_pos1...>>number
is_pos2 =string.find("is",is_pos1+1)
print(is_pos2) #it will also find 2nd is 