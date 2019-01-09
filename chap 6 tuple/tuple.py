# looping in tuple
mixed = (1,2,3,4.0)

 # for loop
for i in mixed:
    print(i)

# tuple with one element
nums = (1)          #not a tuple
words = ('word1')   #  ,,
print(type(nums))   # not a tuple
print(type(words))  #  ,,


num = (1,)           # tuple
print(type(num))     # ,,
word = ('word',)     # tuple
print(type(word))    # ''

# tuple without parantheses
x = 'dd','yy','nn'
print(type(x))

# tuple  unpacking
ys =  ('cc','ff','kk')
y1,y2,y3 = (ys)
print(y1)

# list inside tuple
fav = ('kk',['uu','yy'])
fav[1].pop()
fav[1].append("we do")
print(fav)

# functions
print(max(mixed))
print(min(mixed))
print(sum(mixed))
   