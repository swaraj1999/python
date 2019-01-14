# word counter using dictionary
d={'s':1,'a':2,'r':1,'a':2}              # it will print key'a' once with overwrite of 2nd value

print(d)

def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_counter('swaraj'))