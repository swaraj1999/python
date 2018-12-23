#take two comma separated inputs : name and a character,o/p: length of user name,count the number of charcter that user inputs(will count both capital and small)
name,char =input("user name and enter a single character(separated by comma) :: ").split(",")
print(f"length of users name {len(name)}")
print(f"char count :{name.lower().count(char.lower())}") #case insensitive
#Swaraj > swaraj
#S > s
# name.lower().count(char.lower())