num = int(input("Enter a num:"))
if num & (num-1)==0:
    print("Power of 2")

else:
    print("no")


#another way divide continuously 
# while num:
#     if num == 1:
#          print("Power of 2")
#          break 

#     if num%2==0:
#         num=num//2

#     elif num%2!=0:
#         print("Not power")
#         break
