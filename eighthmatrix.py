fl = True
x = []
while fl:
    m = int(input("Input the first number\n"))
    i = int(input("Input the second number\n"))
    if m == 0:
        fl = False
        break
    else:
        x.append([m, i])
z = []
for i in range(len(x)):
    summa = x[i][0] + x[i][1]
    z.append(summa)
    summa = 0
mxsum = 0
rownum = 0
for m in range(len(z)):
    if z[m] > mxsum:
        mxsum = z[m]
        rownum = m+1

print(f"Max sum of {mxsum} has the row number {rownum}")