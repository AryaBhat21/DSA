#5*5=25 , 
def fun(n,i=1):
    if n<i*i:
        return False
    if n == i*i:
        return True
    return fun(n,i-1)



perfect_sqr = int(input("enter a num: "))
if fun(perfect_sqr):
    print("yes")
else:
    print("no")


    