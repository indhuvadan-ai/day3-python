def fac_rec(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fac_rec(n-1)
    

k= int(input("enter number for factorial\n"))

print(fac_rec(k))