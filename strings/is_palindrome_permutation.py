def isPalindromePermutation(s: str) -> bool:
    hash_map = {}
    odd_count = 0
    for char in s:
        if not char.isalnum():
            continue
        char = char.lower() if char.isalpha() else char
        if char not in hash_map:
            hash_map[char] = 1
            odd_count += 1
            continue
        hash_map[char] += 1
        if hash_map[char] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1

    return odd_count in (0, 1)


if __name__ == '__main__':
    result1 = isPalindromePermutation("A man, a plan, a canal: Panama")
    print(result1)
