arr= [1,1,1,1,2,3,4,4,4,6,6,6,4,9,9,9,9,9,9,9,9]
freq = {}
for i in arr:
    freq[i] = freq.get(i,0)+1

print(freq)