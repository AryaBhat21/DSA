#swap 2 number without temp

num1 = 2
num2 = 4

print(f"{num1}\n{num2}")

num1 , num2 = num2, num1

print(f"{num1}\n{num2}")

#another way 
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print(f"{num1}\n{num2}")
#xor
num1=num1^num2
num2=num1^num2
num1=num1^num2

print(f"{num1}\n{num2}")