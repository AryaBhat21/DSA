#https://codeforces.com/problemset/problem/617/A


x = int(input("pos:"))
if x%5==0:
    print("steps", x//5)
else:
    print("steps",x//5+1)
