 # in keyword and iterations in dictionary

user_info = {
    'name':'swaraj',
    'age':19,
    'fav movies':['ggg','hhh'],
    'fav tunes':['qqq','www'],
}

# check if key in dictionary
if 'name' in user_info:           # check any key word
    print('present')
else:
    print('not present')

# check if value exists in dictionary
if 24 in user_info:
    print('present')
else:
    print('not present')   

# loopps in dictionary
for i in user_info:
    print(i)                  # print keys
    print(user_info[i])       # value

# value method
user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

#  keys method
user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# item method                       
user_items = user_info.items()
print(user_items)
print(type(user_items))
