# 2 to the power 4 = 2*2*2*2
def fun(a,b):
    if b<1:
        return 1
    return a*fun(a,b-1)
    
print(fun(2,0))