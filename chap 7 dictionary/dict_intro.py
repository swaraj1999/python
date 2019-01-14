                               ############################ Dictionary introduction ################################
#   Q >> why we use dictionary ??
# 
#   A >> becuse of limitations of list,lists are not enough to represent data
# 
# 
# example>>
user = ['swaraj',19,['ggg','hhh'],['qqq','www']]
# this list contains user name , age , fav movies , fav tunes
# this is not a prpper way to do this
# 
# 
#   Q >> what are dictionaries ??
#   
#   a >> unordered collection of data in key : value pair
# 
# 
#  how to create dictionaries??

user ={'name':'swaraj','age':19}
print(user)
print(type(user))

#  second method to create  using dict method

user1 = dict(name = 'swaraj',age = 19)
print(user1)

#how to access data from dictionary 
# actualy there is no indexing because of unordered collection of data
print(user['name'])
print(user['age'])

# what can we store in dictionary??
# 
# numbers,string,list,dictionary

user_info = {
    'name':'swaraj',
    'age':19,
    'fav movies':['ggg','hhh'],
    'fav tunes':['qqq','www'],

}
print(user_info['name'])

# how to add data in empty dictionary??
user_info2={}                  #an empty dictionary
user_info2['name'] = 'swaraj'

