n = int(input("Enter a num:"))

x = n
count = 0
#check for count
while x>0:
    count += 1
    x = x//10

armstrong = 0
temp = n
while temp>0:
    dig = temp%10 
    armstrong += dig**count
    temp //=10

if armstrong==n:
    print("hai")
else:
    print(f"iie {armstrong}")
