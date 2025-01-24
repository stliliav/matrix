fl = True
x = []
mn = 1000000000
while fl:
    m = int(input("Input the first number\n"))
    i = int(input("Input the second number\n"))
    if m == 0:
        fl = False
        break
    else:
        x.append([m, i])

for i in range(len(x)):
    for j in range(2):
        if x[i][j] < mn:
            mn = x[i][j]
print(x)
print(mn)
