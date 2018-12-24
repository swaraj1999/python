#ask user for name and age,if name starts with (a or A) and age is above 10 can watch mpovie otherwise sorry
name,age=input("enter \t name \n  \t age ((separated by space)::").split()
age=int(age)
if (age>=10) and (name[0]=='a' or name[0]=='A'):
    print("you can watch movie")
else:
    print("sorry")    