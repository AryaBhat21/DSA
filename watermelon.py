#https://codeforces.com/contest/4/problem/A

weight = int(input("Weight of watermelon:"))

if weight%2==0 and weight>2:
    part = weight//2
    if part%2==0:
        print(part)
    else:
        print(f"{part-1}\t{part+1}")

else:
    print("Indivisble")