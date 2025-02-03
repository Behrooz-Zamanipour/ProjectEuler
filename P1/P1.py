emptySet = set()
for i in range(1001):
    if(i % 3 == 0 or i % 5 == 0):
        emptySet.add(i)
sum = sum(emptySet)
print(emptySet)
print(sum)