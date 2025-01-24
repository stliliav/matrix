fl = True
row = 0
column = 0
x = []
while fl:
    m = int(input("Input the first number\n"))
    i = int(input("Input the second number\n"))
    if m == 0:
        fl = False
        break
    else:
        x.append([m, i])

find = int(input("Input a number that you want to search for:\n"))
for i in range(len(x)):
    for j in range(2):
        if x[i][j] == find:
            row = j+1
            column = i+1
    print(f'Column: {column}\nRow: {row}\n\n')
print(x)