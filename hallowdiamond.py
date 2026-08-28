def main():
    n = 3

    # Outer loop for rows
    for i in range(2 * n - 1):

        comp = 2 * (n - i) - 1 if i < n else 2 * (i - n + 1) + 1

        # Print leading spaces
        for j in range(comp):
            print(' ', end='')

        # Print stars and inner spaces
        for k in range(2 * n - comp):
            if k == 0 or k == 2 * n - comp - 1:
                print('* ', end='')
            else:
                print('  ', end='')

        print()


if __name__ == "__main__":
    main()