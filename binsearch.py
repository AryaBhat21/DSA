values = sorted(list(map(int, input("Enter the numbers:").split())))
print(values)
target = int(input())

low = values[0]
high = len(values)-1
mid = 0

found = False
while low<=high:
    mid = (low+high)//2
    if target == values[mid]:
        print(mid)
        found = True
        break
        
    elif target>values[mid]:
        low = mid +1
    else:
        high = mid

if not found:
    print(-1)
