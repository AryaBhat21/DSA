l = [6,2,5,5,4,5,6,3,7,6]
a = int(input("a:"))
b = int(input("b:"))

c = a+b
sum = 0

if c==0:
    print(6)
else:
    while c>0:
        dig=c%10
        sum+=l[dig]
        c=c//10
    print(sum)

