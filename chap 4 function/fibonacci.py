# fibonacci series
# 0 1 1 2 3 5 8 13 21 34

def fibo_series(n):
    a = 0                     #first number
    b = 1                     #second number
    if n==1:
        print(a)
    elif n==2:
        print(a,b)           # 0 1
    else:
        print(a,b ,  end=" ")   # end = " " for printing other numbers except a,b in same line
        for i in range(n-2):
            c = a+b            #c=1
            a=b                #a=1
            b=c                #b=1
            print(b,end = " ")

fibo_series(10)
