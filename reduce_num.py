num = int(input("Enter a number:"))
def fun(n, c=0):
    if n==1:
        return c
    if n%2==0:
        return fun(n//2, c+1)
    if n%2!=0:
        return min(fun(n+1,c+1),fun(n-1,c+1))
print(fun(num))