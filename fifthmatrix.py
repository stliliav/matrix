fl = True
x = []
k = 0
diagsum = 0
for i in range(3):
    m = int(input("Input the first number\n"))
    i = int(input("Input the second number\n"))
    g = int(input("Input the third number\n"))
    if m == 0:
        break
    else:
        x.append([m, i, g])

for i in range(len(x)):
    diagsum += x[i][i]

print(diagsum)