# s="abc123vd45+"

# alpha = 0
# dig = 0
# for i in s:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         dig += 1
# print("Alphabets: ", alpha)
# print("Digits: ", dig)
        
# s="Arya"
# res=""


# for c in s:
#     if c >= 'a' and c <= 'z':
#         res+=chr(ord(c)-32)
#     else:
#         res+=c

# print(res)

# s="Arya"
# res=""


# for c in s:
#     if c >= 'A' and c <= 'Z':
#         res+=chr(ord(c)+32)
#     else:
#         res+=c

# print(res)


#count of vowels in string
# s="arrhhiiiyyeeaahhhoouuu"
# s=s.lower()
# count = 0
# for ch in s:
#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#         count+=1
# print(count)
# # #another way
# # s = "hello"
# vowels = "aeiouAEIOU"
# c=0
# for ch in s:
#     if vowels.find(ch) != -1:
#     #or if ch in vowels:
#         c+=1
# print(c)


#reverse a string 
# s="aryagbhat"
# n = len(s)
# res=""
# # for ch in range(n-1,-1,-1):
# #     res+=s[ch]
# # print(res)
# # for i in range(n):
# #     res=s[i]+res
# # print(res)
# s=list(s)
# i=0
# j=n-1
# while i<j:
#     s[i],s[j]=s[j],s[i]
#     i+=1
#     j-=1
# l="".join(s)
# print(l)

# s="a#bc$def!"
# s=list(s)
# i=0
# j=len(s)-1

# while i<j:
#     if s[i].isalpha() and s[j].isalpha():
#         s[i],s[j]=s[j],s[i]
#         i+=1
#         j-=1
#     elif not s[i].isalpha():
#         i+=1
#     elif not s[j].isalpha():
#         j-=1
# l="".join(s)
# print(l)

s = "   fly me   to   the moon  "
s = s.replace(" ","")
print(s)








    



    



