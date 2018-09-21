def primes(n):
    numbers = list(range(n))

    for number in numbers:
        if number == 1 or number == 0 or number == -1:
            continue
        else:
            for index in range(number * 2, len(numbers), number):
                numbers[index] = -1

    return numbers


print("n = ", end='')
lst = primes(int(input()))
for num in lst:
    if num != -1:
        print(num)

# HW
# 1. rhomb
# 2. parentheses (stack)
