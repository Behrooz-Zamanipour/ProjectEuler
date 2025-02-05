a = 1
b = 2
sum = b
while(b < 4000000):
    c = b
    b += a
    a = c
    if b < 4000000 and b % 2 == 0:
        sum += b
print(sum)