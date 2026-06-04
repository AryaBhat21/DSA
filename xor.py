#find xor of 1 to n values without using loop 
#1^2^3^4^5

#nums: 0 1 2 3 4 5 6 7 8 9 10 11 12 
#res     1 3 0 4 1 7 0 8 1 11 0 12

num = int(input("enter a num:"))

if num%4 ==0:
    print(num)

elif num%4 == 3:
    print(0)

elif num%4 == 2:
    print(num+1)
    
else:
    print(1)
