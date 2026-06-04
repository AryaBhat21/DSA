s = "My name is AryaGBhat"
len = 0 
count = 0
for i in s:
    if not i.isspace():
        count += 1
    else:
        len = max(count,len)
        count = 0
        
if count > len:
    len = count
print(len)