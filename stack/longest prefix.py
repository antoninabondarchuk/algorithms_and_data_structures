def longestCommonPrefix(strs):
    hash_longest = list(strs[0])
    for word in sorted(strs[1:], key=len):
        for i in range(len(word)):
            if word[i] != hash_longest[i]:
                hash_longest = hash_longest[:i]
                break
            if i == len(word) - 1:
                hash_longest = hash_longest[:i + 1]
    return ''.join(hash_longest)


if __name__ == '__main__':
    result1 = longestCommonPrefix(['flower', 'flow', 'flight'])
    print(result1)
