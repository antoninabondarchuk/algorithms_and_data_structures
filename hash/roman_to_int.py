def romanToInt(s: str) -> int:
    hash_map = {'I': 1, 'V': 5,
                'X': 10, 'L': 50,
                'C': 100, 'D': 500,
                'M': 1000}
    arab_result = 0
    for i in range(len(s) - 1):
        if (hash_map.get(s[i + 1]) > hash_map.get(s[i])):
            arab_result -= hash_map.get(s[i])
        else:
            arab_result += hash_map.get(s[i], 0)
    return arab_result + hash_map[s[-1]]


if __name__ == '__main__':
    result1 = romanToInt('IV')
    print(result1)
