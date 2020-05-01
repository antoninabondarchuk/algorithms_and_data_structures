def to_excel(num):
    capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    result = []
    while num > 0:
        result.append(capitals[(num - 1) % 26])
        num = (num - 1) // 26
    result.reverse()
    return ''.join(result)


if __name__ == '__main__':
    result1 = to_excel(29)
    print(result1)
