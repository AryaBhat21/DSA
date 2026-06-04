arr = [1,2,3,4,5,6,7,8,9,10]
#output arr=[5,4,3,2,1]
n = len(arr)
for i in range(n//2):
    arr[i],arr[n-1-i]=arr[n-1-i],arr[i]

print(arr)

#another way 
# i and j pointer ; such that while i<j: swap -> increment i -> decrement j 