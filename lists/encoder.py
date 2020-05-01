def encode(raw_list, code_words):
    encoded_list = []
    hash_letters = dict()
    for i in range(len(raw_list)):
        if raw_list[i] not in hash_letters:
            hash_letters[raw_list[i]] = code_words[i]
        encoded_list.append(hash_letters[raw_list[i]])

    return encoded_list


if __name__ == '__main__':
    encoded_one = encode(["a"], ["1", "2", "3", "4"])
    encoded_two = encode(["a", "b", "c"], ["1", "2", "3", "4"])
    encoded_three = encode(["a", "b", "a"], ["1", "2", "3", "4"])
    print(encoded_one, encoded_two, encoded_three)
