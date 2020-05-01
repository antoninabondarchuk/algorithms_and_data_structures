def sort_del_duplicates(input_list):
    return list(set(sorted(input_list)))


def pythonic_sort_del(input_list):
    prepared_set = []
    for num in input_list:
        if num not in prepared_set:
            prepared_set.append(num)
    return sorted(prepared_set)


if __name__ == '__main__':
    sorted_equal = sort_del_duplicates([1, 1])
    sorted_equal2 = pythonic_sort_del([1, 1, 2])
    print(sorted_equal)
    print(sorted_equal2)
