def is_balanced(parentheses):
    queue = []
    for ch in parentheses:
        if ch == '(':
            queue.append(ch)
        elif ch == ')':
            if not queue:
                return False
            queue.pop()
        else:
            print('Invalid character found.')
            return False

    return True


print("Enter parentheses: ", end='')
print("Parentheses are balanced:", is_balanced(input()))
