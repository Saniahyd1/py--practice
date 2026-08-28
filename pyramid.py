rows = 5

for i in range(1, rows + 1):
    # Print spaces followed by stars
    print(" " * (rows - i) + "*" * (2 * i - 1))
