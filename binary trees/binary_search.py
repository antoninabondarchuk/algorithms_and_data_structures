def searchInsert(nums, target) -> int:
    lower = 0
    higher = len(nums) - 1
    while lower <= higher:
        mid = int((higher + lower) / 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            lower = mid + 1
        else:
            higher = mid - 1

    return lower


if __name__ == '__main__':
    result1 = searchInsert([1, 2, 4, 6], 5)
    print(result1)
