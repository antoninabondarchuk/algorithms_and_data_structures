def to_binary(num, stack=[]):
    while num >= 2:
        num, remainder = divmod(num, 2)
        stack.append(remainder)
    stack.append(num)
    return ''.join(str(i) for i in stack[::-1])


if __name__ == '__main__':
    result1 = to_binary(1775)
    print(result1)
