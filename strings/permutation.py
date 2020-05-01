def remove_char(string, idx):
    end_idx = idx if idx == len(string) else idx + 1
    return string[:idx] + string[end_idx:]


def get_all_permutations(string):
    if string is None:
        return None
    if len(string) <= 1:
        return {string}
    permutations = set()
    for idx, char in enumerate(string):
        clear_str = remove_char(string, idx)
        words = get_all_permutations(clear_str)
        for word in words:
            permutations.add(char + word)
    return permutations


if __name__ == '__main__':
    result1 = get_all_permutations('string')
    print(result1)
