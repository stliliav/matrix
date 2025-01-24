fl = True
x = []
k = 0
while fl:
    m = int(input("Input the first number\n"))
    i = int(input("Input the second number\n"))
    if m == 0:
        fl = False
        break
    else:
        x.append([m, i])
newx = []
for i in range(len(x)):
    for j in range(2):
        newx.append(x[i][j])
unique = []
for i in range(len(newx)):
    if newx.count(newx[i]) == 1:
        unique.append(newx[i])
print(x)
print(unique)