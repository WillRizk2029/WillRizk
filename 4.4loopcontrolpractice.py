for I in range(20):
    if I == 15:
        break
    print(I)
for I in range(30):
    if I % 2 == 0:
        continue
    print(I)
for x in range(10):
    if x == 5:
        pass
    print(x)
for W in range(10, 0, -1):
    if W == 5:
        continue
    print(W)
list = [4, 7, 8, 13, 14, 17, 26]
sum = 0
for i in list:
    if i < 0:
        break
    sum += i
print(sum)