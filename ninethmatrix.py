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
sum1 = 0
sum2 = 0
for i in range(len(x)):
    sum1 += x[i][0]
    sum2 += x[i][1]

if sum1 > sum2:
    print(f"Min sum of {sum2} has the column number 2")
else:
    print(f"Min sum of {sum1} has the column number 1")
