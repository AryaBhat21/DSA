
l = [1,2,2,3,1,2,3,4,2,5,2]
#1. remove duplicate
# n=[]
# for i in l:
#     if i not in n:
#         n.append(i)
    
# print(n)

#2. find numbers which are repeated for odd number of times
#wrongggg
# n = len(l)
# hash_arr = [0] * n
# x=[]
# for i in range(n):
#     hash_arr[l[i]]+=1

# for i in range(len(hash_arr)):
#     if hash_arr[i]%2!=0:
#         x.append(i)

# print(x)

#another way
# l1 = []
# for i in l:
#     if l.count(i)%2!=0 and i not in l1:
#         l1.append(i) 

# print(l1)

#sort the list in unique way
#if value is even -> asc
#if value is odd -> desc
#then combine 

for i in l:
    if i%2==0:
        







