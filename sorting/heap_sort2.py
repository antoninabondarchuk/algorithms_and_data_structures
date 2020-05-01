from math import ceil


def min_top_heap_sort(array, arr_len, index):
    left_idx = index * 2 + 1
    right_idx = index * 2 + 2

    smallest_idx = index

    if (left_idx < arr_len) and (array[left_idx] < array[smallest_idx]):
        smallest_idx = left_idx

    if (right_idx < arr_len) and (array[right_idx] < array[smallest_idx]):
        smallest_idx = right_idx

    if index != smallest_idx:
        array[index], array[smallest_idx] = array[smallest_idx], array[index]
        min_top_heap_sort(array, arr_len, smallest_idx)


def heap_sort_apply(array):
    arr_len = len(array)

    for i in range(ceil(arr_len / 2), -1, -1):
        min_top_heap_sort(array, arr_len, i)

    print(array)

    for i in range(arr_len - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        min_top_heap_sort(array, i, 0)

    return array


if __name__ == '__main__':
    array = [5, 7, 10, 56, 2, 1, 8]
    result1 = heap_sort_apply(array)
    print(result1)
