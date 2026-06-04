#perfect num : factors of a num excluding itself when added will give the num itself

num = int(input("Enter a number:"))

per =[]
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
        per.append(i)
if sum==num:
    print("perfect num")
    print(per)
else:
    print("Not a perfect num")