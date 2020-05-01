def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    result1 = climbStairs(9)
    print(result1)
