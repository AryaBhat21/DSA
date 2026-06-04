#factorial of each digit of a number gives the number itself
#eg: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)

x = int(input("Enter a number:"))
n = x

sum=0
while n>0:
    dig = n%10
    sum += fact(dig)
    n = n//10

if sum==x:
    print("Strong num")

else:
    print("No")

