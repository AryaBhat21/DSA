#a string s and int k will be given. need to traverse k steps backwards \
s = input("Enter the string: ").lower()
k = int(input("K: "))
ns = ""
for i in s:
    x = chr(ord(i)-k)
    if chr(97) <= x <= chr(122):
        ns += x
    else:
        ns += chr(ord(x)+26)
print(ns)

ns=""
#another way
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    for j in alpha:
        if i==j:
            ns += alpha[(alpha.index(j)-k)]

print(ns)