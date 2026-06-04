#string compression: eg: s=aabbbcc ns=a2b3c2 if ns<s: print ns else print s
s = input("Enter : ")
ns = ""
d = {}

for i in s:
    d[i] = d.get(i,0)+1

for i in d:
    ns += i + str(d[i])

if len(ns)<len(s):
    print(ns)

else:
    print(s)