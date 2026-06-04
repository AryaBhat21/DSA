d={1:"hi",2:"hello",3:"bye","hi":1}
# print(d)
# print(d[1])
# print(d["hi"])
# print(d.get(1))
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.pop(1))
# d.popitem()
# print(d.clear())
# print(d)

# for i in d:
#     print(i, end=" ")
#     print(d[i])

d = {"arya":60,
     "anush":100,
     "deanna":90,
     "krishna":40,
     "adya":75}

nd = {}

for i in d:
    if d[i]>80:
       nd[i] = "A"

    elif d[i]>70:
        nd[i] = "B"

    elif d[i]>60:
        nd[i] = "C"

    else:
        nd[i] = "D" 

print(nd)