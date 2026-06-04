#https://codeforces.com/problemset/problem/791/A
# a = int(input("Enter weight of limak:"))
# b = int(input("Enter weight of bob:"))

a,b = map(int, input("enter:").split())

year = 0
while a<=b:
    a = a*3
    b = b*2
    year+=1
print(year)

    