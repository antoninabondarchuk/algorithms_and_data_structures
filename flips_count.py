def count_flips(num1, num2):
    return (bin(num1 ^ num2)).count('1')


if __name__ == '__main__':
    result1 = count_flips(0b11101, 0b10111)
    print(result1)
