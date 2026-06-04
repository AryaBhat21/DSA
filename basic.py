#check if number is even or odd without using modulous
num = int(input("Enter a number:"))
#even -> 0010 (2)
#odd -> 0011 (3)

if num & 1 == 0:
    print("Even")

else:
    print("Odd")

