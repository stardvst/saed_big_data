def call_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@call_twice
def wow():
    print("wow")


wow()


# max_twice = call_twice(max)
# print(*max_twice(2, 4))


def even(start, end):
    while (start < end):
        start += 2
        yield start
        yield start
        yield start


print(*even(1, 5))


def never_end():
    while True:
        yield 1


for x in never_end():
    print(x)
