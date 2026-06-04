nums=[1,2,3,1,2,4,2,3,1]
k = 4
new = []
for i in range(len(nums)-k+1):
    d={}
    for j in range(i, i+k+1):
        d[nums[j]]=d.get(nums[j],0)+1
    new.append(len(d))

print(new)