# break and continue keyword

# break

for i in range(1,10):
    if i==5:
        break   # i=1 print,i=2 print,i=3 print,i=4 print,i=5 then it will break
    print(i)    # 1,2,3,4

# continue

for i in range(1,11):
    if i==5:
        continue #i=1 print, 2 print, 3 print, 4 print, i= 5 if execute and it will run for loop,i=6 print....
    print(i)     #1,2,3,4,6,7,8,9,10