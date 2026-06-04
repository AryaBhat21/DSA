#eg: n=7:111->3
#eg: 10 and 9 = n increment count, now n and n-1 increment count, 
num = int(input("Enter a num:"))

count = 0
while num>0:
    num = num&(num-1)
    count+=1
print(count)


