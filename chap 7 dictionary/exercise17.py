# take infos in dictionary from user
user={}                                     # blank dict
name=input('name??')                        # inputs from user
age=input('age??')
fav_movie=input('fav movie separated by space').split()

user['name']=name
user['age']=age
user['fav_movie']=fav_movie

print(user)

for key,value in user.items():
    print(f"{key}:{value}")
