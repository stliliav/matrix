fl = True
mx1 = 0
mx2 = 0
x = []
while fl:
    m = int(input("Input the first number\n"))
    i = int(input("Input the second number\n"))
    if m == 0:
        fl = False
        break
    else:
        x.append([m, i])

for i in range(len(x)):
    if x[i][0] > mx1:
        mx1 = x[i][0]
    if x[i][1] > mx2:
        mx2 = x[i][1]
print(f"Max number in the first column: {mx1}\nMax number in the second column: {mx2}")