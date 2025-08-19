def fib_rec(n):
    if n<0:
        raise ValueError("input error! non negative numbers please!")
    elif n<=1:
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)   #cause fibonacci series means sum of previos 2 numbers
    
k=int(input("Enter the length of fibonacci series\n"))

for i in range(k):
    print (fib_rec(i))     #cause only print was giving only final value