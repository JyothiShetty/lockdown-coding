rows = int(input("enter number of rows \n"))
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end='\n')
print(" " "\n")