rows = int(input("Enter how many rows: "))
square = int(input("Enter how many square: "))
rec = int(input("Enter how many rectangle: "))
dia = int(input("Enter how many diamond: "))
ex = int(input("Enter how big x: "))
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()
print()
for s in range(square):
    print("* " * square)
print()
for r in range(rec):
    print("* " * (rec * 2))
print()
for d in range(dia):
    print(" " * (dia - d - 1), end="")
    for i in range(d + 1):
        print("*", end=" ")
    print()
for d in range(dia - 1, -1, -1):
    print(" " * (dia - d - 1), end="")
    for i in range(d + 1):
        print("*", end=" ")
    print()

for x in range(ex):
    for j in range(ex):
        if j == x or j == ex - x - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
