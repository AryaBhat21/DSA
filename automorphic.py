#sqaure of a number lst number shld be the number itself
#eq: 5 -> 25 ends w 5, 25 -> 625 ends w 25

temp= int(input("Enter a num:"))
num = temp
sqr = num*num

#dc
dc = 0
while num>0:
    dc+=1
    num=num//10

count = 10**dc

last = sqr%count

if last == temp:
    print("Automorphic number")

else:
    print("No ")


