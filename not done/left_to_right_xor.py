# l = int(input("Enter the value of l:"))
# r = int(input("Enter the value of r:"))

# xor = 0
# for i in range(l,r+1):
#     xor = xor^i
# print(xor)

def xor(num):
    if num%4==0:
        return num

    elif num%4==1:
        return 1

    elif num%4==2:
        return num+1

    else:
        return 0
l,r= map(int,input("Enter the value of l and r:").split())
a=xor(r)
b=xor(l-1)
print(a^b)
