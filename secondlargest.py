arr=[7,0,-1,-3,5,2,4,6,8,8,10,10]
max1 = arr[0]
max2 = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i]<max2 and arr[i]!=max1:
        max2= arr[i]
        
print(max2)

    