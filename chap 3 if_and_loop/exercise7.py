#sum of n natural numbers ,n will be given by user
n=input("enter no of terms")
n=int(n)
total=0
i=1
while i<=n:
    total+=i
    i+=1
print(f"total is {total}")


# using for loop
for i in range(1,11):
    total+=i
print(total)