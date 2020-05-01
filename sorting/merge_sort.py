def merge_sort(array):
    if len(array) < 2:
        return array
    sorted_array = []
    middle = int(len(array) / 2)
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    left_i = 0
    right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] > right[right_i]:
            sorted_array.append(right[right_i])
            right_i += 1
        else:
            sorted_array.append(left[left_i])
            left_i += 1

    sorted_array.extend(left[left_i:])
    sorted_array.extend(right[right_i:])
    return sorted_array


if __name__ == '__main__':
    sorted1 = merge_sort([1, 7, 5, 3, 4, 2, 0])
    sorted2 = merge_sort([])
    sorted3 = merge_sort('')
    sorted4 = merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(sorted1)
