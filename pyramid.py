for row in range(4):
    print(" " * (4 - row), end="")
    for col in range(row + 1):
        print("* ", end="")
    print()