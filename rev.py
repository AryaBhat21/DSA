n = int(input("Enter a num:"))

rev = 0

while n>0:
    digit = n%10
    rev = digit + rev*10
    n=n//10
    
print(rev)
    
