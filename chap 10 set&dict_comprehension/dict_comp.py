# dictionary comprehension
# square = {1:1,2:4,3:9}              # square value of key       key:value

square={num:num**2 for num in range(1,11)}
print(square)

sqr={f"square of {num} is ":num**2 for num in range(1,11)}
print(sqr)

for k,v in sqr.items():
    print(f"{k}:{v}")


string='swaraj'
#
word_count={char:string.count(char) for char in string}
print(word_count)
## to count letters in name