def rhomb(n):
    rows = ['*']
    for spaces in range(1, n, 2):
        rows.append('*' + ' ' * spaces + '*')

    spaces = n // 2
    for idx, row in enumerate(rows):
        rows[idx] = '{0}{1}'.format(' ' * spaces, row)
        spaces -= 1

    rows = rows[:-1] + rows[::-1]

    return '\n'.join(rows)


if __name__ == '__main__':
    print("n = ", end='')
    try:
        n = int(input())
        if (n > 1):
            print(rhomb(n))
        else:
            print("n must be >= 2.")
    except Exception:
        print("Please enter a number!")
