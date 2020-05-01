from math import ceil


def make_heap(array, array_len, root_index):
    # assume we have largest element as root
    largest_element_index = root_index

    # calculate childrens' indexes
    right_index = root_index * 2 + 2
    left_index = root_index * 2 + 1

    # check if root has children and if one of them is larger that root
    if (left_index < array_len) and (array[largest_element_index] < array[left_index]):
        largest_element_index = left_index

    if (right_index < array_len) and (array[largest_element_index] < array[right_index]):
        largest_element_index = right_index

    # check if we change smth
    if largest_element_index != root_index:
        array[root_index], array[largest_element_index] = array[largest_element_index], array[root_index]
        make_heap(array, array_len, largest_element_index)


def apply_heap_sort(input_array):
    # precalculate length
    array_length = len(input_array)

    # make heap without including leaves (cause they have no leaves)
    for index in range(ceil(array_length / 2), -1, -1):
        make_heap(input_array, array_length, index)

    # min-root sort (bottom-top)
    for index in range(array_length - 1, 0, -1):
        input_array[index], input_array[0] = input_array[0], input_array[index]
        make_heap(input_array, index, 0)


if __name__ == "__main__":
    list_to_sort = [20, 15, 8, 10, 5, 7, 6, 2, 9, 1]
    apply_heap_sort(list_to_sort)
    print(list_to_sort)
