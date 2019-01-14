 # add and delete data
user_info = {
    'name':'swaraj',
    'age':19,
    'fav movies':['ggg','hhh'],
    'fav tunes':['qqq','www'],
}

# how to add
user_info['fav_songs'] = ['song1','song2']
print(user_info)

# pop method
popped_item=user_info.pop('fav tunes')    # at least habe to pass one item
print(f"popped item is{popped_item}")
print(user_info)
print(type(popped_item))                  # return list

# pop item method                         # random delete
pop_item=user_info.popitem()              # no item to pass
print(user_info)
print(type(pop_item))                     # returns tuple

