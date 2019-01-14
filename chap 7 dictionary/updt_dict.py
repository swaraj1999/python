# update a dictionary
user_info = {
    'name':'swaraj',
    'age':19,
    'fav movies':['ggg','hhh'],
    'fav tunes':['qqq','www'],
}

more_info = {'name':'SWARAJ','state':'west bengals','hobbies':['coding']}    #UPDATE NAME ALSO

user_info.update(more_info)
print(user_info)

#user_info.update({})                                                            # it means we have updatw nothing...!!