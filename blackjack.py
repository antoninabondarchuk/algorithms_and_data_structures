"""

Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they both go over.


blackjack(19, 21) → 21
blackjack(21, 19) → 21
blackjack(19, 22) → 19
"""


def blackjack(a, b):
    if a == 21:
        return a
    if b == 21:
        return b
    elif a < 21:
        if b > 21:
            return a
        return b if (21 - b) < (21 - a) else a
    return b if b < 21 else 0


if __name__ == '__main__':
    test_case1 = blackjack(19, 21)
    test_case2 = blackjack(34, 33)
    test_case3 = blackjack(22, 19)

    print(test_case1)
    print(test_case2)
    print(test_case3)
