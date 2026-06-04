#magic number each digits when added until we get 1 as answer
#eg: 1999 -> 1+9+9+9 = 28 -> 2+8 = 10 -> 1+0 = 1 ; thus magic
#eg: 123 -> 1+2+3 = 6 ; thus no 
num = int(input("enter a number: "))
while num>9:
    sum=0
    while num>0:
        d = num%10
        sum += d
        num //= 10

    num = sum

if num == 1:
    print("magic")

else:
    print("no")


