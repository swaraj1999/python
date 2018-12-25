# pallindrome function like madam,
def is_pallindrome(name):
    return name == name[::-1]
    #if name == reverse of name
    #        then true,otherwise false

# print(is_pallindrome(input("enter name")))     #not working for all words
print(is_pallindrome("horse"))                   #working for all words