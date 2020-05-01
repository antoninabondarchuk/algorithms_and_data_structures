def create_hash_map(string):
    hash_map = {}
    for char in string:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    return hash_map


def duplicated_permutation(hash_map, prefix, remaining, result_list):
    if remaining == 0:
        result_list.append(prefix)
        return result_list
    for char in hash_map:
        if hash_map[char] > 0:
            hash_map[char] -= 1
            duplicated_permutation(hash_map, prefix + char, remaining - 1, result_list)
            hash_map[char] += 1
    return result_list


if __name__ == '__main__':
    string = 'aaabc'
    hash_map = create_hash_map(string)
    result = []
    result1 = duplicated_permutation(hash_map, '', len(string), result)
    print(result1)
