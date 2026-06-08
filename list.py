#create input ls to take values using map
ls = list(map(int,input("Enter the numbers:").split()))
#to append
ls.append(10)
print(ls)
#to print without as list
# for i in ls:
#     print(i,end=" ")
#in single lin2
print(*ls)