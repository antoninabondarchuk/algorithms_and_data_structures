def watercount(earth_array):
    earth_len = len(earth_array)
    if earth_len < 3:
        return 0
    total_water = 0
    left_index = 0
    right_index = earth_len - 1
    left_max = earth_array[left_index]
    right_max = earth_array[right_index]
    while left_index <= right_index:
        left_max = max(left_max, earth_array[left_index])
        right_max = max(right_max, earth_array[right_index])
        if left_max <= right_max:
            total_water += left_max - earth_array[left_index]
            left_index += 1
            continue
        total_water += right_max - earth_array[right_index]
        right_index -= 1

    return total_water


if __name__ == '__main__':
    result1 = watercount([2, 1, 3, 2, 1, 3, 5, 4, 3, 0, 4, 0])
    result2 = watercount([0, 0])
    result3 = watercount([])
    result4 = watercount([5, 3, 4, 4, 3])

    print(result1)
    print(result2)
    print(result3)
    print(result4)
