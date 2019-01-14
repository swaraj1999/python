# more about get method
user={'name':'swaraj','age':19}
print(user.get('names','not found'))          # it will print not found instead of none cz names is not key,other wise print value

#more than two  same keys

user={'name':'swaraj','age':19,'age':12}      # it will overwrite 12
print(user)
