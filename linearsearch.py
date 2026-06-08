values = list(map(int, input("Enter the numbers:").split()))
target = int(input())

found = False
for i in range(len(values)):
    if target == values[i]:
        print(i)
        found = True
        break
    
if not found:
    print(-1)