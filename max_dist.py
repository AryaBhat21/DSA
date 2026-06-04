nums=[1,3,2,1,5,8,7,2,9]
d={}
res =0 
diff = 0

for i in range(len(nums)):
    if nums[i] not in d:
        d[nums[i]]=i

    else:
        diff = i- d[nums[i]]
        if diff>res:
            res = diff

print(res)

