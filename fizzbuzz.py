# div by 3 -> fizz
# div by 5 -> buzz
# div by 3 n 5 -> fizzbuzz

num = int(input("Enter a num:"))

if num%3==0:
    if num%5==0:
        print("Fizzbuzz")
    else:
        print("fizz")

elif num%5==0:
    print("Buzz")

else:
    print("None divisible")