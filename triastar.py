n = int(input("Enter a num:"))

# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")  
#     print()


# for i in range(1, 6):
#     if i==3:
#         continue
#     print(i,end=" ")


# for i in range(n):
#     for j in range(n-1,i-1,-1):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print("*", end = "")
#     print()

# 00 01 02 03
# 10       13
# 20       23
# 30 31 32 33

# k=1
# for i in range(n):
#         for j in range(n):
#             if i==0 or j==0 or i==n-1 or j==n-1:
#                 print("*", end=" ") 
#             else:
#                 print(k, end=" ")
#                 k+=1
#         print()
        
# for i in range(n):
#     for j in range(0,n-i-1):
#         print(" ", end=" ")
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()


for i in range(n):
    for j in range(0,i+1):
        print(" ", end=" ")
    for j in range(0,n-i):
        print("*", end=" ")
    print()